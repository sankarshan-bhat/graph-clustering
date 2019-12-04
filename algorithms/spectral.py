import numpy as np
from sklearn.cluster import SpectralClustering
from sklearn import metrics
np.random.seed(0)
#data_path = os.path.join('data', 'network_ICND_1_wo_zero_weights_converted.txt')
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
    A[tup[0], tup[1]] = tup[2]*10
    A[tup[1], tup[0]] = tup[2]*10

adj_mat = [[3,2,2,0,0,0,0,0,0],
           [2,3,2,0,0,0,0,0,0],
           [2,2,3,1,0,0,0,0,0],
           [0,0,1,3,3,3,0,0,0],
           [0,0,0,3,3,3,0,0,0],
           [0,0,0,3,3,3,1,0,0],
           [0,0,0,0,0,1,3,1,1],
           [0,0,0,0,0,0,1,3,1],
           [0,0,0,0,0,0,1,1,3]]

#adj_mat = np.array(adj_mat)

sc = SpectralClustering(100, affinity='precomputed', n_init=100)
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

for k,v in node_map.iteritems():
	print k," : ",v

# get egigen values and plot. 


# node_assignments = list(sc.spectral_clustering(sim_matrix, n_clusters,
#                                                    random_state=1))
#     clusters = []
#     for n in xrange(n_clusters):
#         clusters.append([i for i, m in enumerate(node_assignments) if m == n])
#     if node_map:
#         return [[node_map[n] for n in cl] for cl in clusters]
#     else: return clusters
