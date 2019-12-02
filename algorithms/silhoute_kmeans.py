from sklearn.datasets import make_blobs 
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score 
from sklearn.metrics import davies_bouldin_score 
import sys

# Generating the sample data from make_blobs 

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

edges2 = []
edge_w = []
with open(sys.argv[1]) as f:
    for line in f:
        #print (line)
        x = line.strip().split('\t')
        edges2.append(tuple([int(x[0]), int(x[1])]))
        edge_w.append([int(x[0]),int(x[1]),float(x[2])])
           

# Construct affinity matrix A
nodes2 = np.unique(np.asarray(edges2))
num_nodes2 = nodes2.shape[0]

A = np.zeros([num_nodes2, num_nodes2])
for tup in edge_w:
    A[tup[0], tup[1]] = tup[2]
    A[tup[1], tup[0]] = tup[2]

#no_of_clusters = [5,7,10,20,30,50,100,200,250,300,350,400,450] 
no_of_clusters = [10,20,50,100,150,200,250]  

for n_clusters in no_of_clusters: 
  
    kmeans = KMeans(n_clusters = n_clusters) 
    kmeans.fit(A)
    cluster_labels = kmeans.labels_

  
    # The silhouette_score gives the  
    # average value for all the samples. 
    silhouette_avg = silhouette_score(A, cluster_labels) 
  
    print("For no of clusters =", n_clusters, 
          " The average silhouette_score is :", silhouette_avg) 

    davies_bouldin = davies_bouldin_score(A, cluster_labels)
    print("For no of clusters =", n_clusters, 
          " The  davies_bouldin_score is :", davies_bouldin)