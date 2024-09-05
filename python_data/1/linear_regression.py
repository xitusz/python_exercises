import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas


#############      Pré-processamento     ###############
# Coleta e Integração
file = pandas.read_csv('/home/gabrielalves/Development/python_data/1/dados_dengue.csv')

years = file[['ano']]
cases = file[['casos']]

##############       Mineração        #################
regr = LinearRegression()
regr.fit(X=years, y=cases)

future_year = pandas.DataFrame([[2018]], columns=['ano'])
cases_2018 = regr.predict(future_year)

print('Casos previstos para 2018 ->', int(cases_2018))

############      Pós-processamento     ################
plt.scatter(years, cases, color='black')
plt.scatter(future_year, cases_2018, color='red')
plt.plot(years, regr.predict(years), color='blue')

plt.xlabel('U')
plt.ylabel('Casos de dengue')
plt.xticks([2018])
plt.yticks([int(cases_2018)])

plt.show()