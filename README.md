# Customer Segmentation using K-Means Clustering 🚀

## 📌 Project Overview
This project performs **Customer Segmentation** using the **K-Means Clustering** algorithm. Businesses use customer segmentation to group customers based on similarities, allowing for targeted marketing strategies and personalized services.

## 🔥 Key Features
- **Data Loading:** Reads customer data from a CSV file.
- **Data Preprocessing:** Extracts relevant features (Annual Income & Spending Score) for clustering.
- **Elbow Method:** Determines the optimal number of clusters.
- **K-Means Clustering:** Segments customers into meaningful groups.
- **Visualization:** Generates cluster plots for better insights.

## 🛠 Technologies Used
- **Python**
- **Pandas** (Data Manipulation)
- **Matplotlib & Seaborn** (Data Visualization)
- **Scikit-Learn** (Machine Learning)

## 📊 How It Works
1. Load the dataset (`Mall_Customers.csv`).
2. Preprocess the data by selecting relevant features.
3. Use the **Elbow Method** to determine the best number of clusters.
4. Apply **K-Means Clustering** to segment customers.
5. Visualize the clusters using scatter plots.

## 🚀 Installation & Usage
### Prerequisites:
Ensure you have **Python 3.7+** installed along with the following libraries:
```bash
pip install pandas matplotlib seaborn scikit-learn
```
### Install all the requirements:
```bash
pip install -r requirements.txt
```
### Run the Project:
```bash
python customer_segmentation.py
```

## 📌 Example Output
- **Elbow Method Plot** (to find the optimal number of clusters)
- **Customer Segments Scatter Plot** (visualizing different groups)

## 🎯 Future Improvements
- Extend segmentation to more customer attributes (e.g., Age, Gender)
- Implement **Hierarchical Clustering** for comparison
- Develop a **web-based visualization dashboard**

## 🤝 Contribution
Feel free to fork the repository and submit pull requests for improvements!

## 📄 License
This project is licensed under the **MIT License**.

