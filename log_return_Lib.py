import numpy as np
import pandas as pd
import os

dataset = []
#Import Dataset
for x in range(2004,2023):
    dataset.append(pd.read_csv('{}.csv'.format(x)))

#Define the destination csv files
rft = "log_{}.csv"
rf = []
for i in range(2004,2023):
    rf.append(rft.format(i))

#Generate Matrix to store log return
#itr = -1
#Fmatrix = np.zeros((15,265,29))
log_returns = []
for A in dataset:
    log_data = A.applymap(np.log)
    returns = log_data - log_data.shift(1)
    returns = returns.drop(returns.index[0])
    log_returns.append(returns)
    # nrows, ncols = A.shape
    # X = A.iloc[:,:].values    
    # itr += 1
    # for i in range(1,nrows):
    #     for j in range(0,ncols):
    #         Fmatrix[itr,i-1,j] = np.log(X[i,j])-np.log(X[i-1,j])
i = 0
for returns in log_returns:
    returns.to_csv(rf[i],index=False)
    i += 1

                
# lst = []  
# for A in Fmatrix:
#     x = A
#     p = 265
#     i = 0
#     while i < p:
#         cnt = 0
#         for j in range(0,29):
#             if x[i][j] == 0:
#                 cnt += 1
#         if cnt >= 15:
#             x = np.delete(x, (i), axis=0)
#             i -= 1
#             p -= 1
#         else:
#             i += 1
#     lst.append(x)


# for i in range(0,15):
#     np.savetxt(rf[i], lst[i], delimiter=",")
