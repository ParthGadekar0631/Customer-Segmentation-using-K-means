import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(data, feature_x, feature_y):
    """Visualizes the clustered data."""
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=data[feature_x], y=data[feature_y], hue=data['Cluster'], palette='viridis', s=100, alpha=0.7)
    plt.title('Customer Segments')
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.legend(title='Cluster')
    plt.show()
