import numpy as np
import pandas as pd
import os

dataset = []
start_year = 2004
end_year = 2018
number_years = end_year - start_year + 1
N = 21
window = 265

#Import Dataset
for x in range(start_year,end_year):
    dataset.append(pd.read_csv('{}.csv'.format(x),header=None))

#Define the destination csv files
rft = "{}.csv"
rf = []
for i in range(start_year,end_year):
    rf.append(rft.format(i))

#Generate Time Series
Fmatrix = np.zeros((number_years,window,N))
for A in dataset and p in range(0,number_years):
    nrows, ncols = A.shape
    X = A.iloc[:,:].values  
    for i in range(1,nrows):
        for j in range(0,ncols):
            Fmatrix[p,i-1,j] = np.log(X[i,j])-np.log(X[i-1,j])
                
#Store the time series as CSV            
for i in range(0,number_years-1):
    np.savetxt(rf[i], Fmatrix[i,:,:], delimiter=",")
