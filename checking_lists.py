import matplotlib.pyplot as plt
import pickle
import numpy as np
import seaborn as sb
from datetime import time
import os
import pandas as pd
from scipy.signal import savgol_filter


with open(r"D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\gen_list\max_degree_list", 'rb') as f:
    max_degree = pickle.load(f)

filtered_degree = savgol_filter(max_degree, 30,5)
plt.plot(filtered_degree, color = 'red', label = 'filtered')
plt.plot(max_degree, color = 'pink', label = 'original')
plt.show()

with open(r"D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\gen_list\number_of_nodes", 'rb') as f:
    number_of_nodes = pickle.load(f)

filtered_nodes = savgol_filter(number_of_nodes, 30,5)
plt.plot(filtered_nodes, color = 'red', label = 'filtered')
plt.plot(number_of_nodes, color = 'pink', label = 'original')
plt.show()
