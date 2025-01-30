import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

class CustomerSegmentation:
    def __init__(self, file_path):
        self.file_path = file_path
        self.customer_data = None
        self.X = None

    def load_data(self):
        """Load customer data from CSV file."""
        self.customer_data = pd.read_csv(self.file_path)
        print("Data Loaded Successfully!")
        print(self.customer_data.head())
    
    def preprocess_data(self):
        """Extracts relevant features for clustering."""
        self.X = self.customer_data.iloc[:, [3, 4]].values
    
    def find_optimal_clusters(self):
        """Uses the Elbow Method to determine the optimal number of clusters."""
        wcss = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
            kmeans.fit(self.X)
            wcss.append(kmeans.inertia_)
        
        plt.figure(figsize=(8,5))
        sns.set()
        plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
        plt.title('Elbow Method for Optimal Clusters')
        plt.xlabel('Number of Clusters')
        plt.ylabel('WCSS')
        plt.show()
    
    def apply_kmeans(self, n_clusters=5):
        """Applies K-Means clustering with a specified number of clusters."""
        kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
        self.customer_data['Cluster'] = kmeans.fit_predict(self.X)
        return kmeans
    
    def visualize_clusters(self, kmeans):
        """Plots customer segments based on clustering results."""
        plt.figure(figsize=(10,6))
        for i in range(kmeans.n_clusters):
            plt.scatter(self.X[kmeans.labels_ == i, 0], self.X[kmeans.labels_ == i, 1], label=f'Cluster {i}')
        
        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroids')
        plt.title('Customer Segments')
        plt.xlabel('Annual Income')
        plt.ylabel('Spending Score')
        plt.legend()
        plt.show()

# Usage Example
if __name__ == "__main__":
    segmentation = CustomerSegmentation("Mall_Customers.csv")
    segmentation.load_data()
    segmentation.preprocess_data()
    segmentation.find_optimal_clusters()
    kmeans_model = segmentation.apply_kmeans()
    segmentation.visualize_clusters(kmeans_model)
