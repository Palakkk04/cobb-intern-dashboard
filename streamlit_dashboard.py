
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px

# ---- Title ----
st.title("Customer Segmentation Dashboard 🚀")
st.write("Built using **Streamlit**, **Pandas**, **Scikit-learn**, and **Plotly**.")

# ---- Upload Data ----
st.sidebar.header("Upload your CSV file")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data", df.head())

    # ---- Data Preprocessing ----
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    st.sidebar.write("Numeric Columns Detected:", numeric_cols)

    if len(numeric_cols) < 2:
        st.error("Upload a CSV file with at least 2 numeric columns for clustering.")
    else:
        selected_cols = st.sidebar.multiselect("Select columns for clustering", numeric_cols, default=numeric_cols[:2])
        if len(selected_cols) >= 2:
            X = df[selected_cols].dropna()

            # ---- KMeans Clustering ----
            k = st.sidebar.slider("Select Number of Clusters", 2, 10, 3)
            model = KMeans(n_clusters=k, random_state=42)
            df['Cluster'] = model.fit_predict(X)

            # ---- Visualization ----
            st.write("### Clustered Data", df.head())
            fig = px.scatter(df, x=selected_cols[0], y=selected_cols[1],
                             color=df['Cluster'].astype(str),
                             title="Customer Clusters",
                             labels={"color": "Cluster"})
            st.plotly_chart(fig)

            # ---- Cluster Count Chart ----
            cluster_counts = df['Cluster'].value_counts().sort_index()
            st.write("### Number of Customers per Cluster")
            fig_bar = px.bar(x=cluster_counts.index, y=cluster_counts.values,
                             labels={'x': 'Cluster', 'y': 'Count'}, text=cluster_counts.values)
            st.plotly_chart(fig_bar)

            # ---- Optional: Download clustered data ----
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Clustered Data", csv, "segmented_data.csv", "text/csv")

else:
    st.info("👈 Upload a CSV file from the sidebar to get started.")

# ---- Footer ----
st.markdown("---")
st.caption("Made with ❤️ by a Data Analyst Intern using BTech CSE Core skills.")
