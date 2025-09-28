import streamlit as st
import requests


st.title("COVID-19 Tracker")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://th.bing.com/th/id/OIP.agN4WAQExnbVqYKx9Qf8ZgHaEK?w=318&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
country = st.text_input("Enter country name:", value="Pakistan")
if st.button("Get Data"):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        st.metric("Total Cases", data.get('cases'))
        st.metric("Deaths", data.get('deaths'))
        st.metric("Recovered", data.get('recovered'))
    except requests.HTTPError:
        st.error("Country not found or API returned an error.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")