import pickle
import os
from progress.bar import Bar
from dotenv import load_dotenv
load_dotenv()


def join_txns(block_data):
    # a = 0
    transacciones = []
    bar = Bar('Processing', max=len(block_data))
    for block in block_data:
        # print(a)
        # a = a + 1
        if "txns" in block['block']:

            for txn in block["block"]["txns"]:
                txn['date'] = block['block']['ts']
                txn['block'] = block['block']['rnd']
                transacciones.append(txn)

            bar.next()
        else:
            pass
        bar.finish()
    return transacciones