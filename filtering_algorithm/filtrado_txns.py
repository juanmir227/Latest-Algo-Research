import pickle
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

threshold = 700
init_block = 17600000
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
for address in unique_addresses:
    sent_txns = df[df['Sender Address'] == address]['Sender Address'].tolist()
    received_txns = df[df['Receiver Address'] == address]['Receiver Address'].tolist()
    if address == "389002307":
        print(sent_txns)
        print(received_txns)
    if len(list(set(sent_txns))) == 1 and len(list(set(received_txns))) == 0:
        filtered = filtered[filtered['Sender Address'] != address]
    elif len(list(set(received_txns))) == 1 and len(list(set(sent_txns))) == 0:
        filtered = filtered[filtered['Sender Address']!= address]
    sent.append(len(sent_txns))
    received.append(len(received_txns))
print(filtered.shape[0])

mean_txns = np.mean(sent)
print(mean_txns)
blacklisted_addresses = []
for i, amount in enumerate(sent):
    if amount > threshold*mean_txns:
        blacklisted_addresses.append(unique_addresses[i])

for i, amount in enumerate(received):
    if amount > threshold*mean_txns:
        blacklisted_addresses.append(unique_addresses[i])

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