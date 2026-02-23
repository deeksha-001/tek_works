import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Mall Customer Clustering",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("Mall_Customers.csv")

df = load_data()

FEATURES = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

# --------------------------------------------------
# Scaling
# --------------------------------------------------
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[FEATURES])

# --------------------------------------------------
# Agglomerative Clustering
# --------------------------------------------------
n_clusters = 5
model = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
clusters = model.fit_predict(scaled_data)

df['Cluster'] = clusters

# --------------------------------------------------
# Compute centroids (needed because no predict())
# --------------------------------------------------
centroids = (
    df.groupby('Cluster')[FEATURES]
    .mean()
    .pipe(scaler.transform)
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("🛍️ Mall Customer Segmentation (Agglomerative Clustering)")

# --------------------------------------------------
# Sidebar Inputs
# --------------------------------------------------
st.sidebar.header("Customer Input")

age = st.sidebar.slider("Age", int(df['Age'].min()), int(df['Age'].max()), 30)
income = st.sidebar.slider(
    "Annual Income (k$)",
    int(df['Annual Income (k$)'].min()),
    int(df['Annual Income (k$)'].max()),
    50
)
score = st.sidebar.slider("Spending Score (1-100)", 1, 100, 50)

input_df = pd.DataFrame([[age, income, score]], columns=FEATURES)
input_scaled = scaler.transform(input_df)

# --------------------------------------------------
# Assign cluster (nearest centroid)
# --------------------------------------------------
distances = np.linalg.norm(centroids - input_scaled, axis=1)
predicted_cluster = np.argmin(distances)

# --------------------------------------------------
# Prediction Output
# --------------------------------------------------
st.subheader("🎯 Predicted Cluster")
st.success(f"Customer belongs to **Cluster {predicted_cluster}**")

# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------
with st.expander("📊 View Clustered Dataset"):
    st.dataframe(df.head(20))

# --------------------------------------------------
# 3D Scatter Plot
# --------------------------------------------------
st.subheader("📈 3D Cluster Visualization")

fig = px.scatter_3d(
    df,
    x='Age',
    y='Annual Income (k$)',
    z='Spending Score (1-100)',
    color=df['Cluster'].astype(str),
    title="Customer Clusters (Agglomerative)",
)

fig.add_scatter3d(
    x=[age],
    y=[income],
    z=[score],
    mode='markers',
    marker=dict(size=12, color='red', symbol='diamond'),
    name='Your Input'
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Cluster Distribution
# --------------------------------------------------
st.subheader("📊 Cluster Distribution")

cluster_counts = df['Cluster'].value_counts().sort_index()

fig_pie = go.Figure(
    data=[go.Pie(
        labels=[f"Cluster {i}" for i in cluster_counts.index],
        values=cluster_counts.values,
        hole=0.4
    )]
)

st.plotly_chart(fig_pie, use_container_width=True)

# --------------------------------------------------
# DENDROGRAM
# --------------------------------------------------
st.subheader("🌳 Hierarchical Dendrogram")

linked = linkage(scaled_data, method='ward')

fig, ax = plt.subplots(figsize=(12, 5))
dendrogram(
    linked,
    truncate_mode='lastp',
    p=20,
    leaf_rotation=90,
    leaf_font_size=10,
    ax=ax
)
ax.set_title("Dendrogram (Ward Linkage)")
ax.set_ylabel("Distance")

st.pyplot(fig)

# --------------------------------------------------
# Cluster Statistics
# --------------------------------------------------
st.subheader("📌 Cluster Statistics")

stats = df.groupby('Cluster')[FEATURES].mean()
st.dataframe(stats)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>🛍️ Mall Customer Segmentation using Agglomerative Clustering</p>",
    unsafe_allow_html=True
)
