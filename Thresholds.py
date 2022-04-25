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

file = 'Mean_RF.csv'

years = [x for x in range(start_year,end_year+1)]
stat = []
avg = []

#Calculate static threshold of each years
for y in range(0,number_year):
    temp = 0
    temp=(dataset[y].mean(axis=0))
    temp = temp.tolist()
    stat.append(statistics.mean(temp))
    print(stat[y])

#Calculate dynamic threshold of each years
for y in range(0,number_year):
    temp = 0
    temp=(dataset[y].median(axis=0))
    temp = temp.tolist()
    avg.append(statistics.mean(temp))
    print(avg[y])
    
if os.path.isfile(file):
    os.remove(file)
np.savetxt(file, avg, delimiter=",")
