import hashlib
import json
from time import time
# Create your views here.
class Blockchain:
    def __init__(self):
        #create a variable name chain : it's a list of blocks stored in form of dictionnary
        self.chain = []   
        self.create_block(nonce = 1, previous_hash = '0', synthese={}) 

    def create_block(self,nonce,previous_hash, synthese):
        index = len(self.chain) + 1
        block = {
            'index': index,
            'timestamp':str(time()),
            'nonce': nonce,
            'previous_hash': previous_hash,
            'synthese':synthese
        }
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False
        while not check_nonce:
            hash_code = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_code[0:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        return new_nonce
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode() #.encode() method is used to convert a string into a sequence of bytes
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]

            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            previous_nonce = previous_block['nonce']
            current_nonce = block['nonce']
            hash_code = hashlib.sha256(str(current_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_code[0:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True


BC1 = Blockchain() #create instance

def get_chain(data):
    response = {
        'chain': BC1.chain,
        'len': len(BC1.chain)
    }
    return response

def mine_block(data):
    previous_block = BC1.get_last_block()
    previous_nonce = previous_block['nonce']
    previous_hash = BC1.hash(previous_block)
    new_nonce = BC1.proof_of_work(previous_nonce)
    block = BC1.create_block(new_nonce, previous_hash, data)
    response = {
        'message':'Block mined',
        'block': block
    }
        
    return block

def is_chain_valid():
    is_valid = BC1.is_chain_valid(BC1.chain)
    if is_valid:
        response = {
            'message': 'Blockchain is valid'
        }
    else:
        response = {
            'message': 'Blockchain is invalid'
        }
    return response
