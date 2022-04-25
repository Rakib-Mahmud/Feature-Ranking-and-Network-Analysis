#Import All the packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import os
from sklearn.ensemble import RandomForestRegressor
from skrebate import ReliefF
from skrebate.turf import TuRF
from sklearn_relief import RReliefF 
import xgboost as xgb

dataset = []
X = []
Y = []
start_year = 2004
end_year = 2018
nnodes = 21
number_year = end_year-start_year+1

#Import Dataset
for x in range(start_year,end_year+1):
    dataset.append(pd.read_csv('{}.csv'.format(x),header=None))

#Generate Input Data and Target Data
for data in dataset:
    nrows, nnodes = data.shape
    X.append(data.iloc[0:(nrows-1),:].values)
    Y.append(data.iloc[1:(nrows),:].values)

#Generate CSV files as CSV can't have multiple sheets
rf = []
xgboost = []
relief = []
rft = "Company_rmv(RF){}.csv"
xgboostt = "Company(XGB){}.csv"
relieft = "Company(Relief){}.csv"

#Define the destination csv files
for i in range(0,number_year):
    rf.append(rft.format(i))
    relief.append(relieft.format(i))
    xgboost.append(xgboostt.format(i))
    
#Declare feature ranking matrix
Fmatrix1 = np.zeros((number_year,nnodes,nnodes))
Fmatrix2 = np.zeros((number_year,nnodes,nnodes))
Fmatrix3 = np.zeros((number_year,nnodes,nnodes))

#Generate Feature Ranking Matrix
for (x,y,itr) in zip(X,Y,range(0,number_year)):
    
    #Prepare RandomForest model
    for node in range(0,nnodes):
      print("Calculating RF ranking for node ", node)
      print("And Round is ",itr)
      regressor = RandomForestRegressor(n_estimators = 500, max_features = 'log2', random_state = 0)
      regressor.fit(x,y[:,node])
      Fmatrix1[itr,node,] = regressor.feature_importances_
    
    #Prepare ReliefF model
    for node in range(0,nnodes):
      print("Calculating ReliefF ranking for node ", node)
      print("And Round is ",itr)
#      relief = RReliefF()
      rel = ReliefF()
      rel.fit(x,y[:,node])
      Fmatrix2[itr,node,] = rel.feature_importances_
      relief.fit_transform(x,y[:,node])
      Fmatrix2[itr,node,] = relief.w_   
    
    #Prepare XGBOOST model
    for node in range(0,nnodes):
      print("Calculating XGBoost ranking for node ", node)
      print("And Round is ",itr)
      xg_reg = xgb.XGBRegressor() 
      xg_reg.fit(x,y[:,node])
      Fmatrix3[itr,node,] = xg_reg.feature_importances_

#Save the generated Feature Ranking Matrix
if os.path.isfile(rf and relief and xgboost):
    os.remove(rf)
    os.remove(relief)
    os.remove(xgboost)
    
for i in range(0,number_year):
    np.savetxt(rf[i], Fmatrix1[i,:,:], delimiter=",")
    np.savetxt(relief[i], Fmatrix2[i,:,:], delimiter=",")
    np.savetxt(xgboost[i], Fmatrix3[i,:,:], delimiter=",")
