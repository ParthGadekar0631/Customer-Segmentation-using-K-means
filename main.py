from data_loader import load_data
from clustering import find_optimal_clusters, apply_kmeans
from visualization import plot_clusters

# Define file path and features
file_path = file_path = "C:\\Users\\parth\\Desktop\\Projects\\Customer-Segmentation-using-K-means\\archive\\Mall_Customers.csv"
feature_columns = ['Annual Income (k$)', 'Spending Score (1-100)']

# Load Data
data = load_data(file_path)
if data is not None:
    # Find Optimal Clusters
    find_optimal_clusters(data, feature_columns)
    
    # Apply K-Means Clustering
    clustered_data, model = apply_kmeans(data, feature_columns, n_clusters=5)
    
    # Visualize Clusters
    plot_clusters(clustered_data, feature_columns[0], feature_columns[1])
