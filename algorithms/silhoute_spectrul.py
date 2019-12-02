from sklearn.datasets import make_blobs 
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score 
from sklearn.metrics import davies_bouldin_score 
from sklearn.cluster import SpectralClustering
from sklearn import metrics
import numpy as np
import sys

#np.random.seed(0)

# Generating the sample data from make_blobs 

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

edges2 = []
edge_w = []
with open(sys.argv[1]) as f:
    for line in f:
        #print (line)
        x = line.strip().split()
        edges2.append(tuple([int(x[0]), int(x[1])]))
        edge_w.append([int(x[0]),int(x[1]),float(x[2])])
           

# Construct affinity matrix A
nodes2 = np.unique(np.asarray(edges2))
num_nodes2 = nodes2.shape[0]

A = np.zeros([num_nodes2, num_nodes2])
for tup in edge_w:
    #print tup
    A[tup[0], tup[1]] = tup[2]
    A[tup[1], tup[0]] = tup[2]

#print A.tolist()

#no_of_clusters = [10,20,50,100,150,200,250]  
no_of_clusters = [5,10,50,100,150]   

for n_clusters_no in no_of_clusters: 
  
    sc = SpectralClustering(n_clusters=n_clusters_no, affinity='precomputed')
    sc.fit(A)
    cluster_labels = sc.labels_

  
    # The silhouette_score gives the  
    # average value for all the samples. 
    silhouette_avg = silhouette_score(A, cluster_labels,metric='manhattan') 
    #silhouette_avg = silhouette_score(A, cluster_labels) 

    print("For no of clusters =", n_clusters_no, 
          " The average silhouette_score is :", silhouette_avg) 

    davies_bouldin = davies_bouldin_score(A, cluster_labels)

    print("For no of clusters =", n_clusters_no, 
          " The davies_bouldin_score is :", davies_bouldin)