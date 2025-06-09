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

# Tamper with block1 and see chain break
print("\nAfter tampering with Block 1:")
block1.data = "Modified Data"
print(f"New Block1 hash: {block1.calculate_hash()}")
print(f"Block2's previous hash: {block2.previous_hash}")
print("Blockchain valid?", block1.calculate_hash() == block2.previous_hash)