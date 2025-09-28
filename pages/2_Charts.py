import streamlit as st
from utils import load_data
import matplotlib.pyplot as plt


st.title("Charts & Visualizations")
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

uploaded_file = st.file_uploader("Upload CSV for plotting", type="csv", key="charts")
if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("Preview")
    st.dataframe(df.head())

    # pick numeric columns
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if not num_cols:
        st.warning("No numeric columns found for plotting. Try a different CSV.")
    else:
        plot_type = st.selectbox("Plot type", ["Histogram", "Boxplot", "Scatter"])
        if plot_type == "Histogram":
            col = st.selectbox("Column for histogram", num_cols)
            bins = st.slider("Bins", min_value=5, max_value=100, value=20)
            fig, ax = plt.subplots()
            ax.hist(df[col].dropna(), bins=bins)
            ax.set_title(f"Histogram of {col}")
            st.pyplot(fig)
        elif plot_type == "Boxplot":
            col = st.selectbox("Column for boxplot", num_cols, key="box_col")
            fig, ax = plt.subplots()
            ax.boxplot(df[col].dropna())
            ax.set_title(f"Boxplot of {col}")
            st.pyplot(fig)
        else:  # Scatter
            if len(num_cols) < 2:
                st.warning("Need at least two numeric columns for scatter plot.")
            else:
                x_col = st.selectbox("X column", num_cols, index=0)
                y_col = st.selectbox("Y column", num_cols, index=1)
                fig, ax = plt.subplots()
                ax.scatter(df[x_col], df[y_col])
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f"{y_col} vs {x_col}")
                st.pyplot(fig)
else:
    st.info("Upload a CSV to create charts.")