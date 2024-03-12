import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.previous_hash, timestamp, data)
    while not is_valid_proof(index, previous_block.hash, hash):
        hash = calculate_hash(index, previous_block.previous_hash, timestamp, data)
    return Block(index, previous_block.previous_hash, timestamp, data, hash)

def is_valid_proof(index, previous_hash, hash):
    nonce = 0
    while True:
        value = str(index) + str(previous_hash) + str(nonce)
        new_hash = hashlib.sha256(value.encode('utf-8')).hexdigest()
        if new_hash[:4] == "0000":
            return True
        nonce += 1
    return False

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add new blocks with voting data
voter_id = input("Enter voter ID: ")
voter_vote = input("Enter voter vote: ")
new_block = create_new_block(previous_block, {"voter_id": voter_id, "vote": voter_vote})
blockchain.append(new_block)

# Print the blockchain
print("Blockchain:")
for block in blockchain:
    print(block.__dict__)