from networkx import edge_betweenness_centrality
from random import random
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
import math
import csv
import random as rand
import sys
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import community


import matplotlib
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from collections import Counter

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

if len(sys.argv) < 2:
        sys.stderr.write("Usage: %s <input graph>\n" % (argv[0],))
        sys.exit(1)

graph_fn = sys.argv[1]
G = nx.Graph()  #let's create the graph first
buildG(G, graph_fn, '\t')

comp = girvan_newman(G)

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

values_girvan=[thisdict.get(node) for node in G.nodes()]


dict_nodes_girvan={}
for each_item in thisdict.items():
    community_num=each_item[1]
    community_node=each_item[0]
    
    if community_num in dict_nodes_girvan:
        value=str(dict_nodes_girvan.get(community_num)) + ' | ' + str(community_node)
        dict_nodes_girvan.update({community_num: value})
    else:
        dict_nodes_girvan.update({community_num: str(community_node)})
        
# Creating the output file
community_df_girvan=pd.DataFrame.from_dict(dict_nodes_girvan, orient='index',columns=['Members'])
community_df_girvan.index.rename('Community Num', inplace=True)
community_df_girvan.to_csv('Community_List_girvan_snippet.csv')
# Creating a graph where each node represents a community
G_comm_girvan=nx.Graph()
G_comm_girvan.add_nodes_from(dict_nodes_girvan)

# Calculation of number of communities and modularity
print("Total number of Communities=", len(G_comm_girvan.nodes()))
mod_girv=community.modularity(thisdict,G)
print("Modularity:", mod_girv)

# Creation of the graph
pos_girvan=nx.spring_layout(G)
nx.draw_networkx(G, pos_girvan,cmap=plt.get_cmap('magma'),with_labels=True,node_size=30,font_size=10, node_color=values_girvan,
                 label='Modularity =' + str(round(mod_girv,3)) +', Communities=' + str(len(G.nodes())))



# nx.draw_networkx(G_comm, pos_louvain, with_labels=True,node_size=160,font_size=11,label='Modularity =' + str(round(mod,3)) +
#                     ', Communities=' + str(len(G_comm.nodes())))
# plt.suptitle('Community structure (Louvain Algorithm)',fontsize=22,fontname='Arial')
# plt.box(on=None)
# plt.axis('off')
# plt.legend(bbox_to_anchor=(0,1), loc='best', ncol=1)
# plt.savefig('louvain.png',dpi=400, bbox_inches='tight')

# Now we try to obtain the color coded graph for each community
plt.suptitle('InWeb Protein Protein Interaction Network (Girvan-Newman Algorithm)',fontsize=22,fontname='Arial')
plt.box(on=None)
plt.axis('off')
plt.legend(bbox_to_anchor=(0,1), loc='best', ncol=1)
plt.savefig('Girvan-Newman_InWeb.png', dpi=400, bbox_inches='tight')