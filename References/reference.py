from algosdk.v2client import algod
import json
import os
from dotenv import load_dotenv
load_dotenv()

algod_address = "https://mainnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": os.environ["PURESTAKE_API"],
}

algod_client = algod.AlgodClient(algod_token, algod_address, headers)

try:
    status = algod_client.status()
    print("Status: " + json.dumps(status, indent=2, sort_keys=True))
except Exception as e:
    print("Failed to get algod status: {}".format(e))

# Retrieve latest block information                                                                                                                                               
last_round = status.get("last-round")
print(last_round)
try:
    block = algod_client.block_info(last_round)
    print("Latest block: " + json.dumps(block, indent=2, sort_keys=True))
except Exception as e:
    print("Failed to get algod status: {}".format(e))