import random
from collections import defaultdict

class Validator:
    def __init__(self, name):
        self.name = name
        self.power = random.randint(1, 100)  # For PoW
        self.stake = random.randint(10, 100)  # For PoS (minimum 10 for meaningful stakes)
        self.votes = 0  # For DPoS (will be assigned later)
    
    def __str__(self):
        return (f"{self.name.ljust(8)} | "
                f"Power: {str(self.power).ljust(3)} | "
                f"Stake: {str(self.stake).ljust(3)} | "
                f"Votes: {self.votes}")

def simulate_pow(validators):
    print("\n" + "="*50)
    print("PROOF OF WORK (PoW) SIMULATION".center(50))
    print("="*50)
    
    print("\nValidator Attributes:")
    print("-"*50)
    print("Name     | Power | Stake | Votes")
    print("-"*50)
    for v in validators:
        print(v)
    
    print("\nSelection Logic:")
    print("1. Miners compete using computational power (higher = better)")
    print("2. The validator with the highest power wins the right to create the block")
    print("3. This requires massive energy expenditure for computations")
    
    selected = max(validators, key=lambda v: v.power)
    
    print("\n" + " RESULT ".center(50, "~"))
    print(f"Selected Validator: {selected.name}")
    print(f"Winning Power: {selected.power}")
    print("Reason: Highest computational power in the network")
    print("~"*50)

def simulate_pos(validators):
    print("\n" + "="*50)
    print("PROOF OF STAKE (PoS) SIMULATION".center(50))
    print("="*50)
    
    print("\nValidator Attributes:")
    print("-"*50)
    print("Name     | Power | Stake | Votes")
    print("-"*50)
    for v in validators:
        print(v)
    
    total_stake = sum(v.stake for v in validators)
    print(f"\nTotal Network Stake: {total_stake}")
    
    print("\nSelection Logic:")
    print("1. Validators 'stake' their coins as collateral")
    print("2. Selection probability is proportional to stake amount")
    print("3. No energy-intensive computations needed")
    
    # Weighted random selection
    pick = random.uniform(0, total_stake)
    current = 0
    for v in validators:
        current += v.stake
        if current >= pick:
            selected = v
            break
    
    print("\n" + " RESULT ".center(50, "~"))
    print(f"Selected Validator: {selected.name}")
    print(f"Stake Amount: {selected.stake} ({selected.stake/total_stake:.1%} of total stake)")
    print("Reason: Random selection weighted by stake amount")
    print("~"*50)

def simulate_dpos(validators):
    print("\n" + "="*50)
    print("DELEGATED PROOF OF STAKE (DPoS) SIMULATION".center(50))
    print("="*50)
    
    # Simulate voting (token holders vote randomly)
    token_holders = ["Holder1", "Holder2", "Holder3", "Holder4", "Holder5"]
    for _ in range(100):  # Simulate 100 votes
        voter = random.choice(token_holders)
        candidate = random.choice(validators)
        candidate.votes += 1
    
    print("\nValidator Attributes After Voting:")
    print("-"*50)
    print("Name     | Power | Stake | Votes")
    print("-"*50)
    for v in sorted(validators, key=lambda x: x.votes, reverse=True):
        print(v)
    
    print("\nSelection Logic:")
    print("1. Token holders vote for delegates")
    print("2. Top N validators by votes become block producers")
    print("3. Producers take turns in a round-robin fashion")
    print("4. Typically more efficient than PoW/PoS")
    
    selected = max(validators, key=lambda v: v.votes)
    
    print("\n" + " RESULT ".center(50, "~"))
    print(f"Selected Validator: {selected.name}")
    print(f"Votes Received: {selected.votes}")
    print("Reason: Received the most votes from token holders")
    print("~"*50)

# Create validators
validators = [
    Validator("Alice"),
    Validator("Bob"),
    Validator("Charlie"),
    Validator("Dave"),
    Validator("Eve")
]

# Run simulations
simulate_pow(validators)
simulate_pos(validators)
simulate_dpos(validators)