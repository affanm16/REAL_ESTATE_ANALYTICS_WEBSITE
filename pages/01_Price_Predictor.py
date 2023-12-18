import streamlit as st
import pickle
import pandas as pd
import numpy as np
st.set_page_config(page_title="PRICE_PREDICTOR",page_icon="🔮")
st.title("PRICE PREDICTOR MODULE")
with open('df.pkl','rb') as file:
    df=pickle.load(file)
with open('pipeline.pkl','rb') as file:
    pipeline=pickle.load(file)


st.header('ENTER INPUTS')


#property type
property_type=st.selectbox('PROPERTY TYPE',['flat','house'])

#sector
sector=st.selectbox('SECTOR',sorted(df['sector'].unique().tolist()))

#bedroom
bedroom=float(st.selectbox('NO. OF BEDROOMS',sorted(df['bedRoom'].unique().tolist())))

#bathroom
bathroom=float(st.selectbox('NO. OF BATHROOMS',sorted(df['bathroom'].unique().tolist())))

#balcony
balcony=st.selectbox('NO. OF BALCONIES',sorted(df['balcony'].unique().tolist()))

#agePossession
property_age=st.selectbox('PROPERTY AGE',sorted(df['agePossession'].unique().tolist()))

# built_up_area
built_up_area=float(st.number_input('BUILTUP AREA'))

# servant room
servant_room=float(st.selectbox('SERVANT ROOM',[0.0,1.0]))
servant_room_label = 'Yes' if servant_room == 1.0 else 'No'
st.write(f"Selected SERVANT ROOM: {servant_room_label}")

#store room
store_room=float(st.selectbox('STORE ROOM',[0.0,1.0]))
store_room_label = 'Yes' if store_room == 1.0 else 'No'
st.write(f"Selected STORE ROOM: {servant_room_label}")

#furnishing_type
furnishing_type=st.selectbox('FURNISHING TYPE',sorted(df['furnishing_type'].unique().tolist()))

# luxury_category
luxury_category=st.selectbox('LUXURY CATEGORY',sorted(df['luxury_category'].unique().tolist()))

#  	floor_category
floor_category=st.selectbox('FLOOR CATEGORY',sorted(df['floor_category'].unique().tolist()))


if st.button('PREDICT'):
    #make a data frame
    data = [[property_type, sector,bedroom, bathroom,balcony,property_age,built_up_area,servant_room, store_room,
             furnishing_type,luxury_category,floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)


    #prediction
    base_price=np.expm1(pipeline.predict(one_df))[0]
    low=base_price-0.22
    high=base_price+0.22
    #display
    st.text("The price of the  {} is between {} Cr. and {} Cr.".format(property_type,round(low,2),round(high,2)))