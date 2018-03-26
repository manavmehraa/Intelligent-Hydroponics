from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import requests
import json
import urllib.request
import numpy as np
import pickle


#firebase_url = 'https://hydroponics-2018.firebaseio.com/'
data = pd.read_csv('/home/manav/Downloads/data.csv')


#print (data.head())

#filter_data = data.dropna(axis=0)

#print(filter_data.describe())

y = data.Label

predictors = ['Water Level', 'Humidity',
'LDR']
#'2ndFlrSF',
#'FullBath',
#'BedroomAbvGr',
#'TotRmsAbvGrd']

X = data[predictors]

#print(X.head())

model = RandomForestRegressor()
model.fit(X,y)
#print(model.predict(X)) #to print the predicted values based upon the fitting

#print (mean_absolute_error(y,model.predict(X))) #prints the error between predicted values and acatual values


train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=0)



#print(val_X)
#print(val_y)


#val_X=[[125,66,32]]

train_model = model.fit(train_X,train_y)


value = model.predict(val_X)
print("Predicted Value = ", value)
#print(mean_absolute_error(val_y,model.predict(val_X)))
#score = model.score(X,y)
#print(score)
#train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=0)

filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))



#model.fit(train_X, train_y)
#value = model.predict(val_X)
#print(value)
#print(mean_absolute_error(val_y,value))

#val_X=[[278,43,1]]

#loaded_model = pickle.load(open('/home/manav/Desktop/Manav/Projects/Hydroponics/finalized_model.sav', 'rb'))
#result = loaded_model.score(X,y)
#print(loaded_model.predict(val_X))
#print(result)
