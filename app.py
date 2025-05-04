import streamlit as st
from data_utils import load_data
import sys

from modules import data_exploration, model_training, prediction_page,eda

# Set the page configuration
st.set_page_config(
    page_title = "Climate Trend Predictor",
    page_icon=' ',
    layout = 'wide'
)

# Give the title
st.title("Temperatures Analytics and Predictions")
st.markdown("Historical temperature-specific data analytics and forecasting")
st.markdown("Temperatures data from Nepal")


df = load_data()


# Give the sidebar for the app navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Data Exploration", "EDA", "Model Training", 'Prediction'])


# Display the selected page
if page == "Data Exploration":
    data_exploration.show(df)
elif page == "EDA":
    eda.show(df)
elif page == "Model Training":
    model_training.show(df)
else: # Prediction page
    prediction_page.show(df)


#Displaying my name
st.sidebar.markdown("### Capstone-Project-Developed By Binod Poudel ")