import matplotlib.pyplot as plt
import pickle
import numpy as np
import seaborn as sb
from datetime import time
from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd


def smooth(given_list):
    for i, element in enumerate(given_list):
        if element == given_list[0] or element == given_list[-1]:
            pass
        else:
            element = (given_list[i-1] + element + given_list [i+1])/3
            given_list[i] = round(element,0)


transaction_type_list = ['pay', 'axfer', 'appl','acfg','keyreg', 'afrz']


with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\periodo1_lists_csv\periodo1_data_lists', 'rb') as fp:
    created_apps, total_transaction_amount, total_sender_number, total_receiver_number, total_active_accounts, mean_transaction_amount_per_sender,mean_transaction_amount_per_receiver, mean_amount_of_unique_receiver_for_sender, mean_amount_of_unique_sender_for_receiver, only_sender_accounts,only_receiver_accounts, percent_of_senders_only_senders, percent_of_receivers_only_receivers, percent_of_accounts_only_senders, percent_of_accounts_only_receivers,sender_average_transacted_accounts, receiver_average_transacted_accounts,sender_average_transacted_with_same_accounts, receiver_average_transacted_with_same_accounts,most_frequent_ids, percentage_of_total_transactions_per_asset, unique_senders_per_asset, unique_receivers_per_asset, unique_accounts_per_asset,percentage_of_total_accounts_per_asset, transactions_one_algo, involved_accounts_per_type, involved_senders_per_type, involved_receivers_per_type,percentage_of_total_accounts_per_type, transaction_amount_in_microalgo, closing_transactions_count, more_than_one_algo,more_than_one_algo_percentage, mean_amount_of_algo_sent, percentage_of_all_transactions_per_type, transaction_type_percentages_of_total_transactions, total_activity = pickle.load(fp)

with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\periodo1_lists_csv\periodo1_filtered_total_transaction_percentage', 'rb') as f:
    filtered_total_transaction_percentage = pickle.load(f)

with open(r'D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\periodo1_lists_csv\periodo1_dates', 'rb') as file:
    chunk_dates = pickle.load(file)



data_lists = [created_apps, total_transaction_amount, total_sender_number, total_receiver_number, total_active_accounts, mean_transaction_amount_per_sender,
mean_transaction_amount_per_receiver, mean_amount_of_unique_receiver_for_sender, mean_amount_of_unique_sender_for_receiver, only_sender_accounts,
only_receiver_accounts, percent_of_senders_only_senders, percent_of_receivers_only_receivers, percent_of_accounts_only_senders, percent_of_accounts_only_receivers,
sender_average_transacted_accounts, receiver_average_transacted_accounts,sender_average_transacted_with_same_accounts, receiver_average_transacted_with_same_accounts,
most_frequent_ids, percentage_of_total_transactions_per_asset, unique_senders_per_asset, unique_receivers_per_asset, unique_accounts_per_asset,
percentage_of_total_accounts_per_asset, transactions_one_algo, involved_accounts_per_type, involved_senders_per_type, involved_receivers_per_type,
percentage_of_total_accounts_per_type, transaction_amount_in_microalgo, closing_transactions_count, more_than_one_algo,
more_than_one_algo_percentage, mean_amount_of_algo_sent, percentage_of_all_transactions_per_type, transaction_type_percentages_of_total_transactions,total_activity]



smoothing_lists = [created_apps, total_transaction_amount, total_sender_number, total_receiver_number, total_active_accounts, mean_transaction_amount_per_sender, 
                   mean_transaction_amount_per_receiver, mean_amount_of_unique_receiver_for_sender, mean_amount_of_unique_sender_for_receiver, only_sender_accounts,
                   only_receiver_accounts, percent_of_senders_only_senders,percent_of_receivers_only_receivers, percent_of_accounts_only_senders, percent_of_accounts_only_receivers,
                    sender_average_transacted_accounts, receiver_average_transacted_accounts, sender_average_transacted_with_same_accounts, receiver_average_transacted_with_same_accounts,
                    transactions_one_algo, transaction_amount_in_microalgo, closing_transactions_count, more_than_one_algo, more_than_one_algo_percentage,
                    mean_amount_of_algo_sent]


smoothing_type_lists = [involved_accounts_per_type, involved_senders_per_type, involved_receivers_per_type,percentage_of_total_accounts_per_type, percentage_of_all_transactions_per_type, transaction_type_percentages_of_total_transactions]


for list in smoothing_lists:
    print(list)
    smooth(list)
    print(list)



for list in smoothing_type_lists:
    print(list)
    for type in transaction_type_list:

        for i, element in enumerate(list):
            try:
                if element == list[0] or element == list[-1]:
                    pass
                else:
                    list[i][type] = (list[i-1][type] + element[type] + list[i+1][type])/3
                    list[i][type] = round(list[i][type],0)
            except:
                pass
    print(list)

print(data_lists)
with open(r"D:\Archivos de Programa\Carpetas\Coding\Algorand\Tesis\Tesis\periodo1_lists_csv\periodo1_smooth_list",'wb') as f:
    pickle.dump(data_lists, f)
