--major project
#Dataset Information
#The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other.

#Dataset Information
#The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other.#Attribute Information:

#sepal length in cm
#sepal width in cm
#petal length in cm
#petal width in cm
#class:
#-- Iris Setosa -- Iris Versicolour -- Iris Virginica

#Import modules
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
 
#Loading the dataset
df = pd.read_csv('Iris.csv')
df.head()

# delete a column
df = df.drop(columns = ['Id'])
df.head()

# to display stats about data
df.describe()

# to basic info about datatype
df.info()

# to display no. of samples on each class
df['Species'].value_counts()

# check for null values
df.isnull().sum()

 
#Exploratory Data Analysis
# histograms
df['SepalLengthCm'].hist()

df['SepalWidthCm'].hist()

df['PetalLengthCm'].hist()

df['PetalWidthCm'].hist()

# scatterplot
colors = ['red', 'orange', 'blue']
species = ['Iris-virginica','Iris-versicolor','Iris-setosa']

for i in range(3):
    x = df[df['Species'] == species[i]]
    plt.scatter(x['SepalLengthCm'], x['SepalWidthCm'], c = colors[i], label=species[i])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()

for i in range(3):
    x = df[df['Species'] == species[i]]
    plt.scatter(x['PetalLengthCm'], x['PetalWidthCm'], c = colors[i], label=species[i])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend()

for i in range(3):
    x = df[df['Species'] == species[i]]
    plt.scatter(x['SepalLengthCm'], x['PetalLengthCm'], c = colors[i], label=species[i])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend()

for i in range(3):
    x = df[df['Species'] == species[i]]
    plt.scatter(x['SepalWidthCm'], x['PetalWidthCm'], c = colors[i], label=species[i])
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.legend()

 
 
 
#Coorelation Matrix
#A correlation matrix is a table showing correlation coefficients between variables. Each cell in the table shows the correlation between two variables. The value is in the range of -1 to 1. If two varibles have high correlation, we can neglect one variable from those two.

df.corr()

corr = df.corr()
fig, ax = plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, ax=ax, cmap = 'coolwarm')

#Label Encoder
#In machine learning, we usually deal with datasets which contains multiple labels in one or more than one columns. These labels can be in the form of words or numbers. Label Encoding refers to converting the labels into numeric form so as to convert it into the machine-readable form

# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# df['Species'] = le.fit_transform(df['Species'])
# df.head()

#Model Training
#from sklearn.model_selection import train_test_split
# train - 70
# test - 30
X = df.drop(columns=['Species'])
Y = df['Species']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)

# logistic regression 
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# model training
model.fit(x_train, y_train)

# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)

# knn - k-nearest neighbours
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()

model.fit(x_train, y_train)

# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)

# decision tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

model.fit(x_train, y_train)

# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)

# save the model
import pickle
filename = 'savedmodel.sav'
pickle.dump(model, open(filename, 'wb'))

x_test.head()

load_model = pickle.load(open(filename,'rb'))
load_model.predict([[6.0, 2.2, 4.0, 1.0]])


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # l
import matplotlib.pyplot as plt
# plt.style.use('dark_background')
import seaborn as sns
sns.set_style('darkgrid')inear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
df = pd.read_csv('../input/iris-flower-dataset/IRIS.csv')
df.head()      
df.info()
df.isnull().sum()
 # Visualising different columns wrt species 
plt.figure(figsize = (16,6))
sns.countplot(df['sepal_length'], hue = df['species'], palette = 'inferno')

plt.figure(figsize = (16,6))
sns.countplot(df['sepal_width'], hue = df['species'], palette = 'Reds')

plt.figure(figsize = (16,6))
sns.countplot(df['petal_length'], hue = df['species'], palette = 'magma')

plt.figure(figsize = (16,6))
sns.countplot(df['petal_length'], hue = df['species'], palette = 'Blues')

plt.figure(figsize = (8,8))
sns.scatterplot(x = 'sepal_length', y = 'sepal_width' , data = df , hue = 'species', palette = 'inferno' , s = 60)

plt.figure(figsize = (8,8))
sns.scatterplot(x = 'petal_length', y = 'petal_width' , data = df , hue = 'species', palette = 'magma' , s=60) 

plt.figure(figsize = (8,8))
sns.pairplot(df)

 # Logistic Regression Model
x = df.drop(['species'] , axis = 1)
y = df['species']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3, random_state = 0)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

lr.fit(x_train, y_train)
lr.score(x_train,y_train)

predictions = lr.predict(x_test)
predictions

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)

# Accuracy = 97.7 %


