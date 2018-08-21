import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from pandas import Series, DataFrame

titanic_df = pd.read_csv('train.csv ')
#print(titanic_df)

# Getting the sense what the data types look like
titanic_df.info()

# Representing gender of the people aboard
sbn.factorplot('Sex',data=titanic_df,kind='count')
#plt.show()

# Classifying gender by classes
sbn.factorplot('Pclass', data=titanic_df,kind='count',hue='Sex')
plt.title("Seprating gender by classes")
#plt.show()

# Checking the total null values for Age column
print(titanic_df.Age.isna().sum())

# Calculating the average age value
avg_age= titanic_df.Age.mean()

# Replacing the null values with mean of age
titanic_df.Age = titanic_df.Age.fillna(avg_age)

# Defining a function which will add Person column in csv file representing if it's a child, male or female.
def male_female_child(passenger):
    age,sex = passenger
    if age< 16:
        return 'child'
    else:
        return sex

titanic_df['person'] = titanic_df[['Age', 'Sex']].apply(male_female_child,axis=1)
print(titanic_df.head(10))

sbn.factorplot('Pclass', data=titanic_df,hue='person', kind='count')
plt.show()

# Plotting a histogram. Bins represents the width of the bars
titanic_df['Age'].hist(bins=400 )
plt.show()


