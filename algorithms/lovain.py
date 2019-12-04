import community
import networkx as nx
import matplotlib.pyplot as plt
import sys
import math
import csv
import random as rand
import pandas as pd


# Replace this with your networkx graph loading depending on your format !

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

if len(sys.argv) < 2:
        sys.stderr.write("Usage: %s <input graph>\n" % (argv[0],))
        sys.exit(1)
graph_fn = sys.argv[1]
G = nx.Graph()  #let's create the graph first
buildG(G, graph_fn, '\t')

#first compute the best partition
partition = community.best_partition(G)

#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))


nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()

print('Completed Louvain algorithm .. . . ' )
values=[partition.get(node) for node in G.nodes()]
list_com=partition.values()

# Creating a dictionary like {community_number:list_of_participants}
dict_nodes={}

# Populating the dictionary with items
for each_item in partition.items():
    community_num=each_item[1]
    community_node=each_item[0]
    if community_num in dict_nodes:
        value=str(dict_nodes.get(community_num)) + ' | ' + str(community_node)
        dict_nodes.update({community_num:value})
    else:
        dict_nodes.update({community_num:str(community_node)})

# Creating a dataframe from the diet, and getting the output into excel
community_df=pd.DataFrame.from_dict(dict_nodes, orient='index',columns=['Members'])
print community_df
community_df.index.rename('Community_Num' , inplace=True)
community_df.to_csv('Community_List_louvain.csv')
# matplotlib.rcParams['figure.figsize']= [12, 8]
# G_comm=nx.Graph()

# # Populating the data from the node dictionary created earlier
# G_comm.add_nodes_from(dict_nodes)

# # Calculating modularity and the total number of communities
# mod=community.modularity(partition,G)
# print("Modularity: ", mod)
# print("Total number of Communities=", len(G_comm.nodes()))

# # Creating the Graph and also calculating Modularity
# matplotlib.rcParams['figure.figsize']= [12, 8]
# pos_louvain=nx.spring_layout(G_comm)
# nx.draw_networkx(G_comm, pos_louvain, with_labels=True,node_size=160,font_size=11,label='Modularity =' + str(round(mod,3)) +
#                     ', Communities=' + str(len(G_comm.nodes())))
# plt.suptitle('Community structure (Louvain Algorithm)',fontsize=22,fontname='Arial')
# plt.box(on=None)
# plt.axis('off')
# plt.legend(bbox_to_anchor=(0,1), loc='best', ncol=1)
# plt.savefig('louvain.png',dpi=400, bbox_inches='tight')
# # Now we try to obtain the color coded graph for each community
# nx.draw_networkx(G, pos, cmap=plt.get_cmap('magma'), node_color=values,node_size=30, with_labels=False)
# plt.suptitle('Louviin Algorithm Community Structure',fontsize=22)
# plt.box(on=None)
# plt.axis('off')
# plt.savefig('louvain_2.png',dpi=400, bbox_inches='tight')
# plt.show()

