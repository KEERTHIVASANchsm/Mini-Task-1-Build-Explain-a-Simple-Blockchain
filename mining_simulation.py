import hashlib
import time
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def __str__(self):
        return f"Block {self.index}\nHash: {self.hash}\nPrevious: {self.previous_hash}\nData: {self.data}\nNonce: {self.nonce}\n"

class MiningBlock(Block):
    def mine_block(self, difficulty):
        start_time = time.time()
        target = "0" * difficulty
        attempts = 0
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1
            
        end_time = time.time()
        print(f"Block mined in {end_time-start_time:.2f} seconds")
        print(f"Nonce attempts: {attempts}")
        print(f"Final hash: {self.hash}\n")

# Create genesis block
genesis_block = Block(0, time.time(), "Genesis Block", "0")

# Create second block
block1 = Block(1, time.time(), "Transaction Data 1", genesis_block.hash)

# Create third block
block2 = Block(2, time.time(), "Transaction Data 2", block1.hash)

# Display blockchain
print(genesis_block)
print(block1)
print(block2)

# Mine a block with difficulty 4
print("Mining block with difficulty 4:")
difficulty = 4
block3 = MiningBlock(3, time.time(), "Mined Data", block2.hash)
block3.mine_block(difficulty)