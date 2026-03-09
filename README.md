# 🔗 Build & Explain a Simple Blockchain

A ground-up Python implementation of a blockchain — built to understand the core mechanics of how blocks, hashing, and chain validation actually work, without the abstraction of a framework.

---

## 🧠 What This Is

This project is a minimal but complete blockchain built from scratch. The goal wasn't to build something production-ready — it was to understand *why* blockchain works the way it does, at the code level. Every design decision is intentional and explained.

---

## ⚙️ How It Works

| Component | Description |
|---|---|
| **Block** | Each block stores an index, timestamp, data, previous hash, and its own hash |
| **Hashing** | SHA-256 generates each block's hash from its contents |
| **Chain Validation** | Every block's `previous_hash` is checked against the actual hash of the preceding block |
| **Tamper Detection** | If any block's data is modified, the entire chain from that point becomes invalid |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/KEERTHIVASANchsm/Mini-Task-1-Build-Explain-a-Simple-Blockchain.git
cd Mini-Task-1-Build-Explain-a-Simple-Blockchain

# Run (Python 3.x required — no external dependencies)
python blockchain.py
```

---

## 💡 Key Concepts Demonstrated

- **Immutability** — changing any block breaks all subsequent hashes
- **Consensus logic** — `is_chain_valid()` walks the entire chain and verifies integrity
- **Genesis block** — the first block is hardcoded with no predecessor
- **Proof-of-work foundation** — structure is ready to extend with a difficulty target

---

## 🛠 Tech Stack

- **Language:** Python 3
- **Libraries:** `hashlib`, `datetime` (standard library only)

---

## 📌 Context

Built as part of a structured blockchain learning path — from basic chain mechanics (this project) → wallet cryptography (Mini-Task-2) → smart contract deployment on Ethereum/Polygon → full dApp development on ICP.
