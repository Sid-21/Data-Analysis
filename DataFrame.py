import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import webbrowser

#website = 'https://en.wikipedia.org/wiki/List_of_all-time_NFL_win%E2%80%93loss_records'
# webbrowser.open(website)

# Creating a df with 5 randomn values and 5 columns, updating values of b column to nan
df2 = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),columns=['a', 'b', 'c', 'd', 'e'])
df2['b'][2:4] = None
print(df2['b'].isna().any())


# Reading data from clipboard
nfl_frame = pd.read_clipboard(sep="", engine='python')
print(nfl_frame)

# To retrieve specifies column
print(nfl_frame['First NFL Season'])

# To retrieve columns
DataFrame(nfl_frame,columns=['Rank', 'Team', 'First Season', 'Total Games'])

# To retrieve top specified number of rows
nfl_frame.head(10)

# To retrieve end specified number of rows
nfl_frame.tail(10)

# To qucikly re index a dataframe
# nfl_frame.ix[[ROWS], NEW_COLUMNS]

# To retrieve rows on a particular index
print(nfl_frame.ix[3])

# Adding Specific string value to a specific column in a DataFrame
stadiums = Series(["Levi's stadium"], index=[4])
nfl_frame['Stadium'] = stadiums
print(nfl_frame)

# Delete a cloumn from DataFrame
del nfl_frame['Stadium']
print(nfl_frame)


# Creating DataFrame from dictionaries
data = {'City':['SA','LA','NYC'],'Population':[83700000,33800000, 8400000]}
city_frame = DataFrame(data)
print(city_frame)