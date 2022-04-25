#Import All the packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import random
plt.style.use('fivethirtyeight')

#Number of stocks
nnodes = 375
start_year = 1998
end_year = 2012
number_year = end_year-start_year+1

###retrive datasets
dataset = []
for x in range(0,number_year):
    dataset.append(pd.read_csv('Company(RF){}.csv'.format(x),header=None))
    
###To save into files, declare them first
rf = []
rft = "Network_Year_{}.csv"

#Define the destination csv files
for year in range(start_year,end_year+1):
    rf.append(rft.format(year))
##############################################################
###Generate Adjacency matrix of network graph
##############################################################
Fmatrix = np.zeros((number_year,nnodes,nnodes))#for 15 different years
Fmatrix = Fmatrix.astype(int)
for itr in range(0,number_year):
    thresld = 0.0027
    for i in range(0,nnodes):
        for j in range(0,nnodes):
            
            if dataset[itr].iloc[i,j] > thresld:
                Fmatrix[itr,i,j] = 1

###Save the generated networks. If necessary to delete previous files, do manually
for i in range(0,number_year):
    np.savetxt(rf[i], Fmatrix[i,:,:], delimiter=",")
