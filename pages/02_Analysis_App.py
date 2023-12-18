import pandas as pd
import ast
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pickle
import streamlit as st
import plotly.express as px
import seaborn as sns
st.set_page_config(page_title="ANALYTICS MODULE",page_icon="📊")
st.title("ANALYTICS MODULE")

#geo_map
st.header('PRICE PER SQFT GEO-MAP')
new_df=pd.read_csv('datasets/data_viz1.csv')

numeric_columns = ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
group_df = new_df.groupby('sector')[numeric_columns].mean()



fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
st.plotly_chart(fig,use_container_width=True)


#wordcloud
st.header('FEATURES WORD CLOUD')
wordcloud_df=pd.read_csv('datasets/wordcloud_df.csv')
sector_input=st.selectbox('SECTOR',sorted(wordcloud_df['sector'] .unique().tolist()))
def get_features_for_sector(wordcloud_df, sector_name):
    main_list = []

    # Filter the DataFrame for the specified sector
    sector_df = wordcloud_df[wordcloud_df['sector'] == sector_name]

    # Apply ast.literal_eval on the 'features' column for the specified sector
    for item in sector_df['features'].dropna().apply(ast.literal_eval):
        main_list.extend(item)
    return main_list
result_for_sector=get_features_for_sector(wordcloud_df,sector_input)
sector_feature_text=' '.join(result_for_sector)

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(sector_feature_text)

fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)

# Plot the wordcloud on the created figure
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")


# Show the figure using streamlit's st.pyplot
st.pyplot(fig)

#area vs price
st.header('AREA vs PRICE')
prop_type=st.selectbox('SELECT PROPERTY TYPE',['flat','house'])
if prop_type=='house':
    fig1 =px.scatter(new_df[new_df['property_type']=='house'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1,use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, use_container_width=True)

#pie chart
st.header("BHK PIE CHART")
sector_options=new_df['sector'].unique().tolist()
sector_options.insert(0,'OVERALL')
selected_sector=st.selectbox(" SELECT SECTOR",sector_options)
if selected_sector=='OVERALL':
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector']==selected_sector] , names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)

#boxplot
st.header('SIDE BY SIDE BHK PRICE COMPARISON')
fig3 = px.box(new_df[new_df['bedRoom'] <= 4] , x='bedRoom', y='price')
st.plotly_chart(fig3, use_container_width=True)

#distplot
st.header('SIDE BY SIDE DISTPLOT FOR PROPERTY TYPE')
fig3=plt.figure(figsize=(10,4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='HOUSE')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'],label='FLAT')
plt.legend()
st.pyplot(fig3)
