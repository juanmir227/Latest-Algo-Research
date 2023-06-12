import pickle
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time

#periodo 1: 11000000-14600000
#periodo 2: 14800000-17400000
#periodo 3: 17600000-23000000
#Hice incrementos de 50000 bloques y saque 500 bloques
shortest_paths = []
total_blacklisted_addresses = []
data_frames = []
threshold = 300
number_of_blocks = 500
increment = 50000
init_1 = 11000000
final_1 = 14600000
init_2 = 14800000
final_2 = 17400000
init_3 = 17600000
final_3 = 23000000
stop = 0
initial_number = list(range(init_1, final_1 + increment, increment)) + list(range(init_2, final_2 + increment, increment)) + list(range(init_3, final_3 + increment, increment))
for init_number in initial_number:
    # stop = stop + 1
    # if stop>1:
    #     break
    if 11000000<=init_number<=14600000:
        periodo = '1'
    if 14800000<=init_number<=17400000:
        periodo = '2'
    if 17600000<=init_number<=23000000:
        periodo = '3'
    
    with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\Try_Periods\periodo'+periodo+'_data_frame\df__'+ str(init_number)+"_"+str(number_of_blocks), 'rb') as fp:
        df = pickle.load(fp)

    df = df[df['Sender Address'] != df['Receiver Address']]
    # print(df.shape[0])
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
    # print(temp)

    degree_list = []
    for element in temp:
        degree_list.append(element[1])

    avg_degree = np.mean(degree_list)


    for element in temp:
        if element[1] > avg_degree*threshold:
            print(element)
            blacklisted_addresses.append(element[0])
    start = time.process_time()
    for element in temp:
        if element[0] not in blacklisted_addresses:
            path_accounts = nx.single_source_shortest_path_length(G,element[0])
            path_length = list(path_accounts.values())
            avg_length = np.mean(path_length)
            if avg_length < 1:
                blacklisted_addresses.append(element[0])
    print(time.process_time()-start)
            # print(np.mean(np.array(path_length)))
        
    data_frames.append(filtered)
    total_blacklisted_addresses.append(blacklisted_addresses)

complete_blacklisted_accounts = list(set(sum(total_blacklisted_addresses,[])))


for i,dataframe in enumerate(data_frames):
    for blacklisted_address in complete_blacklisted_accounts:
        dataframe = dataframe[dataframe['Sender Address'] != blacklisted_address]
        dataframe = dataframe[dataframe['Receiver Address'] != blacklisted_address]
        # print(dataframe.shape[0])
    init_number = initial_number[i]
    G = nx.from_pandas_edgelist(dataframe,'Sender Address', 'Receiver Address')

    if 11000000<=init_number<=14600000:
        periodo = '1'
    if 14800000<=init_number<=17400000:
        periodo = '2'
    if 17600000<=init_number<=23000000:
        periodo = '3'
    nx.write_gexf(G,r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo'+periodo+'_gephi\periodo'+periodo+'_'+str(init_number)+'_'+str(number_of_blocks)+'.gexf')
# nx.write_gexf(G,r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\prueba_wa.gexf')

