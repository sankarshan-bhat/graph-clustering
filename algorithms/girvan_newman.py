from networkx import edge_betweenness_centrality
from random import random
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
import math
import csv
import random as rand
import sys
import pandas as pd

def buildG(G, file_, delimiter_):
    #construct the weighted version of the contact graph from cgraph.dat file
    #reader = csv.reader(open("/home/kazem/Data/UCI/karate.txt"), delimiter=" ")
    reader = csv.reader(open(file_), delimiter=delimiter_)
    for line in reader:
        #print line
        if len(line) > 2:
            if float(line[2]) != 0.0:
                #line format: u,v,w
                G.add_edge(int(line[0]),int(line[1]),weight=float(line[2]))
        else:
            #line format: u,v
            G.add_edge(int(line[0]),int(line[1]),weight=1.0)

def most_central_edge(G):
	centrality = edge_betweenness_centrality(G)
	max_cent = max(centrality.values())
	# Scale the centrality values so they are between 0 and 1,
	# and add some random noise.
	centrality = {e: c / max_cent for e, c in centrality.items()}
	# Add some random noise.
	centrality = {e: c + random() for e, c in centrality.items()}
	return max(centrality, key=centrality.get)
	G = nx.path_graph(10)

if len(sys.argv) < 2:
        sys.stderr.write("Usage: %s <input graph>\n" % (argv[0],))
        sys.exit(1)
graph_fn = sys.argv[1]
G = nx.Graph()  #let's create the graph first
buildG(G, graph_fn, '\t')

comp = girvan_newman(G, most_valuable_edge=most_central_edge)
com=0
thisdict={}

# Populating the items of the dictionary
for c in next(comp):
    list=sorted(c)
    for i in range(len(list)):
        if list[i] in thisdict:
            print('already found')
        else:
            thisdict.update({list[i]: com})
        i+=1
    com+=1

dict_nodes_girvan={}
for each_item in thisdict.items():
    community_num=each_item[1]
    community_node=each_item[0]
    
    if community_num in dict_nodes_girvan:
        value=dict_nodes_girvan.get(community_num) + ' | ' + str(community_node)
        dict_nodes_girvan.update({community_num: value})
    else:
        dict_nodes_girvan.update({community_num: community_node})
        
# Creating the output file
community_df_girvan=pd.DataFrame.from_dict(dict_nodes_girvan, orient='index',columns=['Members'])
community_df_girvan.index.rename('Community Num', inplace=True)
community_df_girvan.to_csv('Community_List_girvan_snippet.csv')