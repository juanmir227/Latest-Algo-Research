import matplotlib.pyplot as plt
import pickle
import numpy as np
import seaborn as sb
from datetime import time
import os
import pandas as pd

with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo1_lists\periodo1_dates', 'rb') as file:
    periodo1_dates = pd.read_pickle(file)
with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo2_lists\periodo2_dates', 'rb') as file:
    periodo2_dates = pd.read_pickle(file)
with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo3_lists\periodo3_dates', 'rb') as file:
    periodo3_dates = pd.read_pickle(file)
with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\gen_list\number_of_nodes', 'rb') as file:
    number_of_nodes = pd.read_pickle(file)

dates = periodo1_dates + periodo2_dates + periodo3_dates
mean_price = []
price_data = pd.read_csv(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\Algo_price_data\algo_price_data.csv')
for date in dates:
    date_row = price_data[price_data['Date'] == str(date)]
    date_mean_price = (float(date_row['Open']) + float(date_row['Close']))/2
    mean_price.append(date_mean_price)
corr_coef = np.corrcoef(mean_price, number_of_nodes)[0,1]

plt.plot(dates, mean_price/np.max(mean_price), label = 'price')
plt.plot(dates,number_of_nodes/np.max(number_of_nodes), label = 'number of nodes')
plt.legend()
plt.xlabel('Date')
plt.ylabel('price-number of nodes')
plt.title('Number of nodes vs price correlation')
plt.text(0,0,f'Corr Coef ={corr_coef}')
plt.show()
print(corr_coef)

plt.plot(dates, number_of_nodes)
plt.show()