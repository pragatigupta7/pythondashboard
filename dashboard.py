# streamlit run dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

# loading data
@st.cache_data
def load_data():
    df = pd.read_csv("Sales Data.csv")
    
    df.columns = [str(name).lower() for name in df.columns.tolist()]
    
    #df['total'] = df[sales].sum(axis=1)
    #df = df.sort_values(by='total', ascending=False)
    return df

# configure the layout
st.set_page_config(
    layout="wide",
    page_title ="Ecommerce sales Analysis",
    page_icon="🛍️",
)
# loading the data
with st.spinner("Loading Data..."):
    df = load_data()
    st.sidebar.success("Data Loaded Successfully! 🎉")

c1, c2 = st.columns([2,2])
c1.title("Ecommerce sales Analysis")

