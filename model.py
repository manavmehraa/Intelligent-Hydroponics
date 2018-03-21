from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import requests
import json
import urllib.request
import numpy as np


firebase_url = 'https://hydroponics-2018.firebaseio.com/'
data = pd.read_csv('/home/manav/Downloads/data.csv')

data = data[20:]
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

print("Predicted Value = ")
val_X=[[421,35,0]]

#print(val_X)
#print(val_y)




train_model = model.fit(train_X,train_y)


value = model.predict(val_X)
print(value)
#print(mean_absolute_error(val_y,model.predict(val_X)))

#train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=0)



#model.fit(train_X, train_y)
#value = model.predict(val_X)
#print(value)
#print(mean_absolute_error(val_y,value))














a = value.size
i=0

#while a>0:
   # data = {'value': value[i]}
    #requests.post(firebase_url + '/' + '/value.json', data=json.dumps(data))
    #print(value[i])
   # a-=1
   # i+=1

#with urllib.request.urlopen("https://hydroponics-2018.firebaseio.com/.json?print=pretty&format=export&download=hydroponics-2018-export.json&auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MjE2MTc0MTksImV4cCI6MTUyMTYyMTAxOSwidiI6MCwiYWRtaW4iOnRydWV9.UBxEYISB9ebjsVv3_p3PrepoBa0gZ0P51YfVLyF3DRQ") as url:
 #   data = json.loads(url.read().decode())



#for key in data["value"]:
 #   print(data["value"][key]["value"])
    	
   
 
