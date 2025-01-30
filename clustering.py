from sklearn.cluster import KMeans

def find_optimal_clusters(data, feature_columns, max_clusters=10):
    """Uses the Elbow Method to determine the optimal number of clusters."""
    from matplotlib import pyplot as plt
    wcss = []
    X = data[feature_columns].values
    
    for i in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    
    plt.figure(figsize=(8,5))
    plt.plot(range(1, max_clusters + 1), wcss, marker='o', linestyle='--')
    plt.title('Elbow Method for Optimal Clusters')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.show()

def apply_kmeans(data, feature_columns, n_clusters=5):
    """Applies K-Means clustering and adds the cluster labels to the dataset."""
    X = data[feature_columns].values
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    data['Cluster'] = kmeans.fit_predict(X)
    return data, kmeans