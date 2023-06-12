import pickle
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

threshold = 300
init_block = 21000000
number_of_blocks = 500

with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\periodo3_data_frame\df__'+ str(init_block)+"_"+str(number_of_blocks), 'rb') as fp:
    df = pickle.load(fp)


df = df[df['Sender Address'] != df['Receiver Address']]
print(df.shape[0])
sender_address = df["Sender Address"].tolist()
receiver_address = df['Receiver Address'].tolist()
total_addresses = sender_address + receiver_address
unique_addresses = list(set(total_addresses))
sent = []
received = []
filtered = df
prefiltered = df
# for address in unique_addresses:
#     sent_txns = df[df['Sender Address'] == address]['Sender Address'].tolist()
#     received_txns = df[df['Receiver Address'] == address]['Receiver Address'].tolist()
#     if len(list(set(sent_txns))) == 1 and len(list(set(received_txns))) == 0:
#         filtered = filtered[filtered['Sender Address'] != address]
#     elif len(list(set(received_txns))) == 1 and len(list(set(sent_txns))) == 0:
#         filtered = filtered[filtered['Sender Address']!= address]
#     sent.append(len(sent_txns))
#     received.append(len(received_txns))
# print(filtered.shape[0])

#tengo que crear la condicion sobre el degree de cada uno
blacklisted_addresses = []
G = nx.from_pandas_edgelist(prefiltered,'Sender Address', 'Receiver Address')
temp = list(G.degree())
degree_list = []
for element in temp:
    degree_list.append(element[1])
avg_degree = np.mean(degree_list)
print(avg_degree)
for element in temp:
    if element[1] > avg_degree*threshold:
        blacklisted_addresses.append(element[0])

print(blacklisted_addresses)

final_filtered = filtered

for blacklisted_address in blacklisted_addresses:
    final_filtered = final_filtered[final_filtered['Sender Address'] != blacklisted_address]
    final_filtered = final_filtered[final_filtered['Receiver Address'] != blacklisted_address]
print(final_filtered.shape[0])

G = nx.from_pandas_edgelist(final_filtered,'Sender Address', 'Receiver Address')
nx.write_gexf(G,r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\gephiprueba.gexf')
# print(np.mean(sent))
# print(np.mean(received))
# G = nx.from_pandas_edgelist(df,'Sender Address', 'Receiver Address')
# print(nx.degree(G))
# nx.write_gexf(G,r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\prueba.gexf')