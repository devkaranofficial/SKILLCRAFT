import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Importing Data
df = pd.read_csv("Mall_Customers.csv")
# print(df.columns)
# print(df)

#From DataFrame Lets store the data we require(Annual Income and Spending Score) into a variable(x)
x = df.iloc[:,[3,4]].values

#Finding WCSS values For 1 to 20 clusters, Elbow Methood
wcss = []
for i in range(1,16):
    k_means=KMeans(
        n_clusters= i ,
        init='k-means++' , 
        random_state=43
    )
    k_means.fit(x)
    wcss.append(k_means.inertia_)

#Plotting graph
plt.figure(figsize=(10,10))
plt.plot(range(1,16) , wcss , marker = 'o')
plt.title("Elbow Graph")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.savefig("elbow_method.png")
plt.show() 

#Final KModel
k_means = KMeans(
    n_clusters=5,
    init='k-means++',
    random_state=43
)
c_kmeans = k_means.fit_predict(x)

#Printing Number Of Clusters
print("Cluster_Centers:")
print(k_means.cluster_centers_)

#Plotting cluster centres
plt.figure(figsize=(10,10))
plt.scatter(
    x[c_kmeans == 0 , 0],
    x[c_kmeans == 0 , 1],
    s = 50 , 
    label = 'Cluster 1'
)
plt.scatter(
    x[c_kmeans == 1 , 0],
    x[c_kmeans == 1 , 1],
    s = 50 , 
    label = 'Cluster 2'
)
plt.scatter(
    x[c_kmeans == 2 , 0],
    x[c_kmeans == 2 , 1],
    s = 50 , 
    label = 'Cluster 3'
)
plt.scatter(
    x[c_kmeans == 3 , 0],
    x[c_kmeans == 3 , 1],
    s = 50 , 
    label = 'Cluster 4'
)
plt.scatter(
    x[c_kmeans == 4 , 0],
    x[c_kmeans == 4 , 1],
    s = 50 , 
    label = 'Cluster 5'
)
plt.scatter(k_means.cluster_centers_[:,0],
            k_means.cluster_centers_[:,1],
            s = 200,
            marker = 'X',
            label = "Cluster Centers")
plt.title("Customer Segmentation using K-Means")
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.savefig("customer_clusters.png")
plt.show()