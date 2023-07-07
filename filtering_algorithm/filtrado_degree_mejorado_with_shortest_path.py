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
init_transaction_amount = []
end_transaction_amount = []
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
periodo1 = list(range(init_1, final_1 + increment, increment))
periodo2 = list(range(init_2, final_2 + increment, increment))
periodo3 = list(range(init_3, final_3 + increment, increment))
initial_number = periodo1 + periodo2 + periodo3
for init_number in initial_number:
    # if stop>0:
    #     break
    # stop = stop + 1

    if init_1<=init_number<=final_1:
        periodo = '1'
    if init_2<=init_number<=final_2:
        periodo = '2'
    if init_3<=init_number<=final_3:
        periodo = '3'
    
    with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\Try_Periods\periodo'+periodo+'_data_frame\df__'+ str(init_number)+"_"+str(number_of_blocks), 'rb') as fp:
        df = pickle.load(fp)
    init_transaction_amount.append(len(df['Sender Address'].tolist()))
    df = df[df['Sender Address'] != df['Receiver Address']]

    sender_address = df["Sender Address"].tolist()
    receiver_address = df['Receiver Address'].tolist()
    total_addresses = sender_address + receiver_address
    unique_addresses = list(set(total_addresses))
    sent = []
    received = []
    filtered = df

    #tengo que crear la condicion sobre el degree de cada uno
    blacklisted_addresses = []
    G = nx.from_pandas_edgelist(filtered,'Sender Address', 'Receiver Address')
    temp = list(G.degree())

    degree_list = []
    for element in temp:
        degree_list.append(element[1])

    avg_degree = np.mean(degree_list)

    for element in temp:
        if element[1] > avg_degree*threshold:
            # print(element)
            blacklisted_addresses.append(element[0])
    #pruebo algo nuevo
    for element in temp:    
        if element[0] not in blacklisted_addresses and element[1]>avg_degree*10:
            # if element[1] > avg_degree*40:
            path_accounts = nx.single_source_shortest_path_length(G,element[0])
            path_length = list(path_accounts.values())
            avg_length = np.mean(path_length)
            if avg_length < 1:
                blacklisted_addresses.append(element[0])


        
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
    component_list = list(nx.connected_components(G))
    lengths = [len(i) for i in component_list]
    for component in component_list:
        if len(component)<max(lengths):
            for element in component:
                dataframe = dataframe[dataframe['Sender Address'] != element]
                dataframe = dataframe[dataframe['Receiver Address'] != element]
    G = nx.from_pandas_edgelist(dataframe,'Sender Address', 'Receiver Address')
    if 11000000<=init_number<=14600000:
        periodo = '1'
    if 14800000<=init_number<=17400000:
        periodo = '2'
    if 17600000<=init_number<=23000000:
        periodo = '3'
    end_transaction_amount.append(len(dataframe['Sender Address'].tolist()))
    # nx.write_gexf(G,r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo'+periodo+'_gephi\periodo'+periodo+'_'+str(init_number)+'_'+str(number_of_blocks)+'.gexf')
    # dataframe.to_pickle(r"D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo"+periodo+'_dataframe\periodo'+periodo+'_'+str(init_number)+"_"+str(number_of_blocks))
#Hasta aca funciona perfectamente ya lo habia probado
print(len(end_transaction_amount))
percentage_1 = []
percentage_2 = []
percentage_3 = []
# init_period_amount_1 = init_transaction_amount[:len(periodo1)]
# print(init_period_amount_1)
# end_period_amount_1 = end_transaction_amount[:len(periodo1)]
# print(end_period_amount_1)
# init_period_amount_2 = init_transaction_amount[len(periodo1)+1:len(periodo1)+1+len(periodo2)]
# print(init_period_amount_2)
# end_period_amount_2 = end_transaction_amount[len(periodo1)+1:len(periodo1)+1+len(periodo2)]
# print(end_period_amount_2)
# init_period_amount_3 = init_transaction_amount[len(periodo1)+1+len(periodo2)+1:]
# print(init_period_amount_3)
# #aca esta el problema
# end_period_amount_3 = end_transaction_amount[len(periodo1)+1+len(periodo2)+1:]
# print(end_period_amount_3)

init_period_amount_1 = init_transaction_amount[:73]
print(init_period_amount_1)
end_period_amount_1 = end_transaction_amount[:73]
print(end_period_amount_1)
init_period_amount_2 = init_transaction_amount[73:126]
print(init_period_amount_2)
end_period_amount_2 = end_transaction_amount[73:126]
print(end_period_amount_2)
init_period_amount_3 = init_transaction_amount[126:]
print(init_period_amount_3)
#aca esta el problema
end_period_amount_3 = end_transaction_amount[126:]
print(end_period_amount_3)
#
for i in range(len(init_period_amount_1)):
    percentage_1.append(end_period_amount_1[i]/init_period_amount_1[i]*100)
for i in range(len(init_period_amount_2)):
    percentage_2.append(end_period_amount_2[i]/init_period_amount_2[i]*100)
for i in range(len(init_period_amount_3)):
    percentage_3.append(end_period_amount_3[i]/init_period_amount_3[i]*100)




print(percentage_1)
print(percentage_2)
print(percentage_3)

#me guardo percentage 1, 2, 3
with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo1_lists\periodo1_filtered_percentage_of_total_transactions', 'wb') as f:
    pickle.dump(percentage_1, f)
with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo2_lists\periodo2_filtered_percentage_of_total_transactions', 'wb') as f:
    pickle.dump(percentage_2, f)
with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\filtering_algorithm\periodo3_lists\periodo3_filtered_percentage_of_total_transactions', 'wb') as f:
    pickle.dump(percentage_3, f)
