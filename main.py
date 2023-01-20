from web3 import Web3
import time

#eth node
web3 = Web3(Web3.HTTPProvider(''))

#contract abi
contarct_abi = ''

#your address
sender_address = ''

#private key
private_key = ''

#contract address
contract_address = ''

#token contract
tokenToBuy = web3.toChecksumAddress('')

#weth contract
spend = web3.toChecksumAddress('') 

contract = web3.eth.contract(contract_address, abi=contarct_abi)
nonce = web3.eth.get_transaction_count(sender_address)
start = time.time()

#tokens amount
tokens_amount = 1

transcation_dict = {
    'from': sender_address, 
    'value': web3.toWei(0.05, 'ether'),
    'gas': 250000,
    'gasPrice': web3.toWei('20', 'gwei'),
    'nonce': nonce,
}

contract_intrct = contract.functions.swapETHForExactTokens(
    tokens_amount * 1000000,
    [spend, tokenToBuy],
    sender_address,
    (int(time.time()) + 10000) 
).buildTransaction(transcation_dict)

signed_txn = web3.eth.account.signTransaction(contract_intrct, private_key)

txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

print(txn_hash.hex())
