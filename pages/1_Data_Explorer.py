import streamlit as st
from utils import load_data


st.title("Data Explorer")
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


uploaded_file = st.file_uploader("Upload a CSV for exploration", type="csv", key="explorer")
if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("Data preview")
    st.dataframe(df)

    # Simple column filter
    col = st.selectbox("Choose a column to filter (optional)", [None] + list(df.columns))
    if col:
        vals = df[col].dropna().unique().tolist()
        selected = st.multiselect(f"Select {col} values to keep", vals)
        if selected:
            filtered = df[df[col].isin(selected)]
        else:
            filtered = df
    else:
        filtered = df

    st.subheader("Filtered data")
    st.dataframe(filtered)

    # Download filtered
    csv = filtered.to_csv(index=False).encode('utf-8')
    st.download_button("Download filtered CSV", data=csv, file_name="filtered.csv", mime="text/csv")
else:
    st.info("Upload a CSV to begin exploring.")