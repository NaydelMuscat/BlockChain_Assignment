from flask import Flask, request, jsonify
from flask_cors import CORS
from web3 import Web3
import json
import os

backend = Flask(__name__)
CORS(backend)

# Connect to local Ethereum node (Ganache on port 7545)
web3  = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Set up the contract instances with the latest ABI
with open(os.path.join(os.path.dirname(__file__), '..', 'build', 'contracts', 'BattleToken.json')) as f:
    battle_token_abi = json.load(f)['abi']

with open(os.path.join(os.path.dirname(__file__), '..', 'build', 'contracts', 'VictoryToken.json')) as f:
    victory_token_abi = json.load(f)['abi']

battle_token = web3 .eth.contract(address='0x1797079519c9f19611525E23FcC45F87d1dC7C20', abi=battle_token_abi)
victory_token = web3 .eth.contract(address='0xF1B25ee672351E59F93760e9F7EE599DA3f16906', abi=victory_token_abi)

@backend.route('/mint', methods=['POST'])
def mint():
    print("Request data:", request.json)
    required_fields = ['account', 'private_key', 'to']
    for field in required_fields:
        if field not in request.json:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    account = request.json['account']
    private_key = request.json['private_key']
    to = request.json['to']
    
    nonce = web3 .eth.get_transaction_count(account)
    txn = battle_token.functions.mint(to).build_transaction({
        'chainId': 1337,
        'gas': 2000000,
        'gasPrice': web3 .to_wei('50', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    logs = battle_token.events.Minted().process_receipt(receipt)
    token_id = logs[0]['args']['tokenId']
    
    return jsonify({'tx_hash': tx_hash.hex(), 'token_id': token_id})

@backend.route('/battle', methods=['POST'])
def battle():
    required_fields = ['account', 'private_key', 'token_id1', 'token_id2']
    for field in required_fields:
        if field not in request.json:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    account = request.json['account']
    private_key = request.json['private_key']
    token_id1 = int(request.json['token_id1'])
    token_id2 = int(request.json['token_id2'])

    owner_of_token1 = battle_token.functions.ownerOf(token_id1).call()
    print(f"Owner of token {token_id1}: {owner_of_token1}")

    if owner_of_token1 != account:
        return jsonify({'error': f'Account {account} is not the owner of token {token_id1}. Owner is {owner_of_token1}'}), 400

    nonce = web3.eth.get_transaction_count(account)
    txn = battle_token.functions.battle(token_id1, token_id2).build_transaction({
        'chainId': 1337,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return jsonify({'tx_hash': tx_hash.hex()})

if __name__ == '__main__':
    backend.run(debug=True)
