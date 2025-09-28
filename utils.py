import streamlit as st
import pandas as pd


@st.cache_data
def load_data(uploaded_file):
    """Load CSV from an uploaded file-like object and cache it.
    Use st.cache_data so repeated uploads or re-runs are fast.
    """
    return pd.read_csv(uploaded_file)