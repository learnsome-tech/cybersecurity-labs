# Cybersecurity Fundamentals, GRC & Cryptography — lesson m04l02 — Data States: Security at Rest, in Transit, and in Use
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l02
# © LearnSome.tech
import random, sqlite3
rng = random.Random(2026)  # fixed seed so this video repeats; use secrets
vault = sqlite3.connect(":memory:")  # really a separate, locked-down service
vault.execute("CREATE TABLE vault (token TEXT PRIMARY KEY, pan TEXT UNIQUE)")

def tokenise(pan):
    cur = vault.execute("SELECT token FROM vault WHERE pan=?", (pan,))
    if found := cur.fetchone():
        return found[0]
    token = "tok_" + "".join(rng.choices("0123456789abcdef", k=16))
    vault.execute("INSERT INTO vault VALUES (?, ?)", (token, pan))
    return token
def mask(pan):
    return "*" * (len(pan) - 4) + pan[-4:]

orders = [(1001, "4111111111111111"), (1002, "5555555555554444"),
          (1003, "4111111111111111")]
for order_id, pan in orders:
    print(order_id, "stored as", tokenise(pan), "support sees", mask(pan))
token = tokenise(orders[1][1])  # the payments service asks the vault
cur = vault.execute("SELECT pan FROM vault WHERE token=?", (token,))
print("vault lookup by payments service:", cur.fetchone()[0])
