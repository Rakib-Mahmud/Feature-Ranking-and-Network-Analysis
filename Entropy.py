#Import All the packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics
import os
plt.style.use('fivethirtyeight')

start_year = 2004
end_year = 2018
number_year = 15
nnodes = 375

#retrive datasets
dataset = []
for x in range(0,number_year):
    dataset.append(pd.read_csv('Company(RF){}.csv'.format(x),header=None))

file = 'Entropy.csv'

years = [x for x in range(start_year,end_year+1)]
entropy = []
    
########################
##Shannon Entropy
#######################
for data in dataset:
    Shannon = 0
    for x in range(0,nnodes):
        pA = data.iloc[x,:]
        Shannon += -np.sum(pA*np.log2(pA))
    e = Shannon/nnodes
    entropy.append(e)
    


if os.path.isfile(file):
    os.remove(file)
np.savetxt(file, entropy, delimiter=",")
