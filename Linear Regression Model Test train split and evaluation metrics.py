import pandas
import numpy
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pyplot
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.model_selection import train_test_split

data = pandas.read_csv('engine_mileage_data.csv')
print(data)

x = data[['Engine_Size','Weight','Horsepower']]
print(x)

y = data['Miles_per_Gallon']
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=10)

model = LinearRegression()
model.fit(x_train, y_train)

predicted_y = model.predict(x_test)

r2 = r2_score(y_test, predicted_y)
mae = mean_absolute_error(y_test, predicted_y)

print("R² Score:", r2)
print("Mean Absolute Error:", mae)
