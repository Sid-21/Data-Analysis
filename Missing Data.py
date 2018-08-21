import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Checking if there is null values in Series
data = Series(['one','two',np.nan,'four'])
print("THis is series",data)
print("This is data.isnull",data.isnull())
# If any null, it's gonna drop
data.dropna()

# Checking if dframe1 has null values. If so, then drop all those rows having null values
dframe1 = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
print("THis is dframe1 \n",dframe1)
clean_dframe= dframe1.dropna()
print("THis is clean_dframe \n",clean_dframe)

# HOW='ALL' will drop rows having all the null values
print("THis is dframe1 \n",dframe1)
print(dframe1.dropna(how='all'))


nan= np.nan
dframe2 = DataFrame([[1,2,3,nan],[2, nan,5,6],[nan,7,nan,9],[1, nan,nan,nan]])
print("This is dataframe 2 \n", dframe2)

# Thres specify minimum data values to be present in a dataset
thres = dframe2.dropna(thresh=3)
print("This is thresh",thres)
print("This is dataframe 2 \n", dframe2)

