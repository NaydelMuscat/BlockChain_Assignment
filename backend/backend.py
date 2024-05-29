from flask import Flask, jsonify, request
from web3 import Web3
import json

app = Flask(__name__)

# Connect to local Ganache blockchain
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Ensure connection to blockchain is successful
if not web3.isConnected():
    raise Exception("Unable to connect to Ganache")

# Set the default account (deployer account)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Load the BattleToken contract ABI and address
with open('../build/contracts/BattleToken.json') as f:
    battle_token_json = json.load(f)
    battle_token_abi = battle_token_json['abi']
    battle_token_address = battle_token_json['networks']['5777']['address']

battle_token = web3.eth.contract(address=battle_token_address, abi=battle_token_abi)

@app.route('/mint', methods=['POST'])
def mint():
    to_address = request.json['to']
    tx_hash = battle_token.functions.mint(to_address).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return jsonify({'message': 'Token minted successfully'})

@app.route('/battle', methods=['POST'])
def battle():
    token_id1 = request.json['tokenId1']
    token_id2 = request.json['tokenId2']
    tx_hash = battle_token.functions.battle(token_id1, token_id2).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return jsonify({'message': 'Battle completed successfully'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)