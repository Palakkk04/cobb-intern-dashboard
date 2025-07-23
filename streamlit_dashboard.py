import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px
import os

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")
st.title("📊 COBB Italy Internship Dashboard")

# Sidebar: Upload or use default sample
st.sidebar.header("Upload Data (optional)")
uploaded = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.success("✅ Uploaded your file!")
else:
    default_path = os.path.join(os.getcwd(), "sample_data.csv")
    df = pd.read_csv(default_path)
    st.info("Loaded default company sample data.")

# Show data preview
st.subheader("🔍 Data Preview")
st.dataframe(df.head())

# Select numeric columns for clustering
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
if len(numeric_cols) < 2:
    st.error("Need at least 2 numeric columns for clustering.")
    st.stop()

x_axis = st.sidebar.selectbox("X-axis:", numeric_cols, index=0)
y_axis = st.sidebar.selectbox("Y-axis:", numeric_cols, index=1)
clusters = st.sidebar.slider("Number of clusters:", 2, 10, 4)

# K-Means clustering
X = df[[x_axis, y_axis]].dropna()
model = KMeans(n_clusters=clusters, random_state=42)
df['Cluster'] = model.fit_predict(X)

# Visualizations
st.subheader("📈 Cluster Scatter Plot")
scatter_fig = px.scatter(df, x=x_axis, y=y_axis, color=df['Cluster'].astype(str),
                         title=f"{clusters} Clusters: {x_axis} vs {y_axis}",
                         labels={'color': 'Cluster'})
st.plotly_chart(scatter_fig, use_container_width=True)

st.subheader("📊 Cluster Distribution")
count_df = df['Cluster'].value_counts().reset_index()
count_df.columns = ['Cluster', 'Count']
bar_fig = px.bar(count_df, x='Cluster', y='Count', title="Records per Cluster")
st.plotly_chart(bar_fig, use_container_width=True)

st.subheader("📁 Clustered Data Sample")
st.dataframe(df.head(10))

# Download option
csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download Clustered CSV", csv_data, file_name="clustered_data.csv")
