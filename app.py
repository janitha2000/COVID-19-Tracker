import streamlit as st
from utils import load_data


st.set_page_config(page_title="🦠COVID-19 Tracker", layout="wide")


st.title("🦠COVID-19 Tracker")

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

# --- Simple Interest Calculator
st.header("Simple Interest Calculator")

principal = st.number_input("Enter Principal:", min_value=0.0, format="%f")
rate = st.number_input("Interest Rate (%):", min_value=0.0, format="%f")
time = st.slider("Time (years):", 1, 10, value=1)

# Button must have indented block under it
if st.button("Calculate Interest"):
    interest = (principal * rate * time) / 100
    st.success(f"Simple Interest: {interest}")



st.markdown("---")


# --- CSV uploader and preview (quick)
st.header("Quick CSV Viewer")
uploaded_file = st.file_uploader("Upload a CSV (or use the pages for more features)", type="csv")
if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("Preview of CSV (first 100 rows)")
    st.dataframe(df.head(100))
    if st.checkbox("Show summary statistics"):
        st.write(df.describe(include='all'))


st.markdown("---")


# --- Session State example
st.header("Session State Counter")
if "count" not in st.session_state:
    st.session_state.count = 0
col1, col2 = st.columns(2)
with col1:
    if st.button("Add"):
        st.session_state.count += 1
with col2:
    if st.button("Reset"):
        st.session_state.count = 0
st.write("Counter value:", st.session_state.count)


st.markdown("---")


st.info("Tip: To see multi-page features, look inside the `pages/` folder. Each file there becomes a separate page automatically.")