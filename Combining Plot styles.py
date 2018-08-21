import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series

# Stats
from scipy import stats

# For plotting
import matplotlib as mplt
import matplotlib.pyplot as plt
import seaborn as sns

# Plotting a combine plot with hist and rug
dataset1 = randn(100)
sns.distplot(dataset1,bins=25)
#plt.show()

# Plotting only KDE plot
sns.distplot(dataset1,bins=25,rug=True,hist=False)
#plt.show()

# For manipulating the presentation of plots
sns.distplot(dataset1,bins=25,
             kde_kws={'color':'indianred','label':'KDE PLOT'},
             hist_kws={'color':'blue', 'label':'HIST'})
plt.show()

# Plotting graph through Series
ser1 = Series(dataset1,name='My_data')
sns.distplot(ser1,bins=25)
plt.show()