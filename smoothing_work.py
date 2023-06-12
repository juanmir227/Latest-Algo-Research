import matplotlib.pyplot as plt
import pickle
import numpy as np
import seaborn as sb
from datetime import time
import os
import pandas as pd

with open(r"D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\periodo1_lists_csv\periodo1_smooth_list", 'rb') as f:
    smooth = pickle.load(f)

with open(r"D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\periodo1_lists_csv\periodo1_data_lists", 'rb') as f:
    lists = pickle.load(f)

print(smooth[0])
print(lists[0])