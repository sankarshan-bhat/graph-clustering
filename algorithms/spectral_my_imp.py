import numpy as np
from sklearn.cluster import SpectralClustering
from sklearn import metrics
import json
import sys

#np.random.seed(0)
#data_path = os.path.join('data', 'network_ICND_1_wo_zero_weights_converted.txt')
edges2 = []
edge_w = []

fn = sys.argv[1]
with open(fn) as f:
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


#adj_mat = np.array(adj_mat)
no_of_clusters = [10,20,50,100,150,200,250]  

for n_clusters in no_of_clusters: 

	print ("running for",n_clusters)
	sc = SpectralClustering(n_clusters=n_clusters, affinity='precomputed')
	sc.fit(A)



	print('spectral clustering')
	print (type(sc.labels_))
	#print (len(sc.labels_))
	#print(sc.labels_.tolist())
	node_map = {}
	cluster = sc.labels_.tolist()

	for i in range(len(cluster)):
		if cluster[i] in node_map:
			node_map[cluster[i] ].append(i) 
		else:
			node_map[cluster[i] ] = []
			node_map[cluster[i] ].append(i) 

	filename = "spetrul_res/2_PPI/"+str(n_clusters)+".json"
	with open(filename, 'w') as outfile:
		json.dump(node_map,outfile)

# get egigen values and plot. 


# node_assignments = list(sc.spectral_clustering(sim_matrix, n_clusters,
#                                                    random_state=1))
#     clusters = []
#     for n in xrange(n_clusters):
#         clusters.append([i for i, m in enumerate(node_assignments) if m == n])
#     if node_map:
#         return [[node_map[n] for n in cl] for cl in clusters]
#     else: return clusters
