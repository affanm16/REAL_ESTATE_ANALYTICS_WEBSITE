import streamlit as st
import pickle
import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Real Estate Analytics", page_icon="🏡")

# Page Title
st.title("Welcome to Real Estate Analytics")

# Introduction
st.write(
    "Explore insights and predictions for real estate in Gurgaon. "
    "Our analytics platform is designed to provide valuable information "
    "about properties, pricing, and recommendations."
)

# Price Predictor Module
st.header("1. Price Predictor")
st.write(
    "Predict the price range of a house or flat by providing details such as property type, "
    "number of bedrooms, bathrooms, and more. Our trained model will provide an estimated price range."
)

# Analysis App Module
st.header("2. Analysis App")
st.write(
    "Visualize and analyze real estate data with our interactive analysis app. Key features include:"
)

# Subpoints for Analysis App
st.subheader("Price per sqft Geo Map")
st.write("View the price per sqft across all sectors of Gurgaon using a color-coded map.")

st.subheader("Word Cloud Visual")
st.write(
    "Generate a word cloud of property features for a specific sector, providing insights into common amenities."
)

st.subheader("Area vs Price Scatter Plot")
st.write("Explore the relationship between property area and price with a scatter plot.")

st.subheader("Other Visualizations")
st.write(
    "Additional visuals include pie charts, box plots, and distribution plots for various attributes of the data."
)

# Recommender System Module
st.header("3. Recommender System")
st.write(
    "Discover relevant properties and societies with our advanced recommender system. Key features include:"
)

# Subpoints for Recommender System
st.subheader("Location-Based Filtering")
st.write(
    "Find apartments within a specified radius of a landmark using our location-based filtering."
)

st.subheader("Combined Recommender")
st.write(
    "Combine three recommenders based on top facilities, price details, and landmarks. "
    "Weighted recommendations provide a holistic view of societies in Gurgaon."
)

# Conclusion
st.header("Get Started!")
st.write(
    "Start exploring Gurgaon's real estate landscape. Use the navigation bar to access the different modules "

)
