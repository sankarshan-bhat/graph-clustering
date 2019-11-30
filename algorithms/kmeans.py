import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

edges2 = []
edge_w = []
with open("network_ICND_1_wo_zero_weights_converted.txt") as f:
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
    A[tup[0], tup[1]] = tup[2] *10
     A[tup[1], tup[0]] = tup[2]*10

#plt.scatter(A[:,0],A[:,1], label='True Position')
kmeans = KMeans(n_clusters=50)
kmeans.fit(A)
print(kmeans.cluster_centers_)
#print(kmeans.labels_)

node_map = {}
cluster = kmeans.labels_.tolist()
for i in range(len(cluster)):
	if cluster[i] in node_map:
		node_map[cluster[i] ].append(i) 
	else:
		node_map[cluster[i] ] = []
		node_map[cluster[i] ].append(i) 

for k,v in node_map.iteritems():
	print k," : ",v

#plt.scatter(A[:,0],A[:,1], c=kmeans.labels_, cmap='rainbow')


#plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
#plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')



# get centroid and plot