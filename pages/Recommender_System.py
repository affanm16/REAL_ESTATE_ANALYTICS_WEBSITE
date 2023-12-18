import streamlit as st
import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pickle
import streamlit as st


st.set_page_config(page_title="RECOMMENDER",page_icon="💡")
st.title("RECOMMENDER SYSTEM")
st.header("LOCATION BASED FILTERING")


location_df=pickle.load(open('datasets/location_distance.pkl','rb'))

selected_location=st.selectbox('LOCATION',sorted(location_df.columns.to_list()))
selected_radius=st.number_input('RADIUS(Kms)')

if st.button('SEARCH'):
    result_series = location_df[location_df[selected_location] < selected_radius * 1000][
        selected_location].sort_values()

    if result_series.empty:
        st.text("NO PROPERTIES FOUND!")
    else:
        for key, value in result_series.items():
            st.text(str(key) + "  " + str(round(value / 1000)) + ' Kms')

st.header("RECOMMEND APARTMENTS")
selected_apartment=st.selectbox("SELECT AN APARTMENT",sorted(location_df.index.to_list()))

cosine_sim1=pickle.load(open('datasets/cosine_sim1.pkl','rb'))
cosine_sim2=pickle.load(open('datasets/cosine_sim2.pkl','rb'))
cosine_sim3=pickle.load(open('datasets/cosine_sim3.pkl','rb'))


def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.5 * cosine_sim2 + 1 * cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df

if st.button('RECOMMEND'):
    recommendation_df=recommend_properties_with_scores(selected_apartment)

    st.dataframe(recommendation_df)


