
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd

data = pd.read_csv('/home/manav/Downloads/train.csv')

print (data.describe())

filter_data = data.dropna(axis=0)

# print(filter_data.describe())

y = data.SalePrice


iowa_predictors = ['LotArea', 'YearBuilt',
'1stFlrSF',
'2ndFlrSF',
'FullBath',
'BedroomAbvGr',
'TotRmsAbvGrd']

X = data[iowa_predictors]


iowa_model = DecisionTreeRegressor()

iowa_model.fit(X,y)

print(iowa_model.predict(X.head()))


