import pickle
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#periodo 1: 11000000-14600000
#periodo 2: 14800000-17400000
#periodo 3: 17600000-23000000
#Hice incrementos de 50000 bloques y saque 500 bloques


threshold = 300
number_of_blocks = 500
increment = 50000
init_1 = 11000000
final_1 = 14600000
init_2 = 14800000
final_2 = 17400000
init_3 = 17600000
final_3 = 23000000
initial_number = list(range(init_1, final_1 + increment, increment)) + list(range(init_2, final_2 + increment, increment)) + list(range(init_3, final_3 + increment, increment))
for init_number in initial_number:
    if 11000000<=init_number<=14600000:
        periodo = '1'
    if 14800000<=init_number<=17400000:
        periodo = '2'
    if 17600000<=init_number<=23000000:
        periodo = '3'
    
    with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\Try_Periods\periodo'+periodo+'_data_frame\df__'+ str(init_number)+"_"+str(number_of_blocks), 'rb') as fp:
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
    nx.write_gexf(G,r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo'+periodo+'_gephi\periodo'+periodo+'_'+str(init_number)+'_'+str(number_of_blocks)+'.gexf')
