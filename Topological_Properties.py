import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import random
plt.style.use('fivethirtyeight')

nnodes = 21
data1 = []

for x in range(2004,2019):
    data1.append(pd.read_csv('Network_{}.csv'.format(x),header=None))

names = pd.read_csv('Company_Names.csv',header=None,encoding = "ISO-8859-1")
rows,cols = names.shape

######################################################
#Calculate total number of connections of every nodes
######################################################
connections = np.zeros((15,nnodes,1))#for 15 different years
connected_to = np.zeros((15,nnodes,1))

#to calculate the number of those nodes that have impact on this node
for itr in range(0,15):
    for i in range(0,nnodes):
        connections[itr,i,] = np.sum(data1[itr].iloc[i,:])

#to calculate the number of those nodes that have impact of this node
for itr in range(0,15):
    for i in range(0,nnodes):
        connected_to[itr,i,] = np.sum(data1[itr].iloc[:,i])

######################################################
#Code to find out community for calculating modularity(Same type company,same community)
######################################################
mapper = {}
community = []  
count = 0
for i in range(0,rows):
    if names[2][i] not in mapper.keys():
        mapper[names[2][i]] = count
        community.append([])
        count += 1
        
for i in range(0,rows):
    community[mapper[names[2][i]]].append(i)

#Top central nodes
def get_top_keys(dictionary, top):
    items = dictionary.items()
    temp =  [k for k, v in sorted(items, key=lambda item: item[1],reverse=True)]
    return (temp[:top])


########################################################
###plot the network and calculate network properties
########################################################
def show_graph_with_labels(adjacency_matrix,label):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(),cols.tolist())
    G = nx.DiGraph() #to find modularity, turn digraph into graph
    G.add_edges_from(edges)
nx.draw(G,node_size=850,labels=label,with_labels=1,edge_color='b',style='dashed',font_color='white',width=0.15) #node_size=150,
#    m = nx.average_clustering(G) #for average clustering coefficient
#    m = nx.average_shortest_path_length(G) #for average shortest path
    # modularity = list(nx.algorithms.community.greedy_modularity_communities(G)) #for modularity
#    modularity = nx.algorithms.community.asyn_fluid.asyn_fluidc(G,k=10)
    m = nx.algorithms.community.modularity(G,community) #for modularity
#    m = nx.algorithms.assortativity.degree_assortativity_coefficient(G,x='out',y='in')
#    m = nx.algorithms.centrality.betweenness_centrality(G)
#    m = nx.algorithms.link_prediction.jaccard_coefficient(G)
#    m = nx.classes.function.density(G) #network density
#    d = nx.algorithms.assortativity.average_neighbor_degree(G)# mean degree
#    m = sum(d.values())/nnodes
#    
    # Connected components are sorted in descending order of their size
#    cam_net_components = list(G.subgraph(c) for c in nx.connected_components(G))
#    cam_net_mc = cam_net_components[0]
#    # Betweenness centrality
#    m = nx.betweenness_centrality(cam_net_mc)
#    m = nx.algorithms.efficiency_measures.global_efficiency(G) #global effiency
#    m = nx.algorithms.centrality.global_reaching_centrality(G) #hirarachy
#    m = nx.algorithms.clique.graph_number_of_cliques(G)
#    m = shortest_path/coeff
    plt.show()
    return m

####################################################
#Find network properties for 15 years
####################################################
clustering_coef1 = []

shortest_path1 = []

modularity1 = []

assortativity1 = []

betweenness_centrality = []

density1 = []

mean_degree1 = []

efficiency1 = []

reaching1 = []


for i in range(0,15):
    modutarity = show_graph_with_labels(data1[i].iloc[:,:],names.iloc[:,0])
#    clustering_coef.append(avg_clus_coeff)
    modularity1.append(modutarity)
#    print(avg_clus_coeff+ "   " +avg_shortest)
    print(modularity)

#Top 10 central company
top_bet_cen = get_top_keys(betweenness_centrality[4],10)
