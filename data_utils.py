import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder

@st.cache_data
def load_data():
    ''' Loading the data from data Temperature.csv'''
    df = pd.read_csv('C:/Users/Sony Vaio/Desktop/all-omdena-file/omdena-6-capstone/capstone-project-binodpoudel/data/Temperature.csv')
    # Convert the date column to datetime
    df['Date']= pd.to_datetime(df['Date'])
    # Extract the features 
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day
    return df


def prepare_features(df):
    """
    Prepare features for model training

    """
    # Features and target
    features = ['year', 'month']
    target = 'Temp_2m'
    X = df[features]
    y = df[target]

    return X, y