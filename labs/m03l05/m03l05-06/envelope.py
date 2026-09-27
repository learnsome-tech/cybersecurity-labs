# Cybersecurity Fundamentals, GRC & Cryptography — lesson m03l05 — Post-Quantum Cryptography & Key Lifecycles
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l05
# © LearnSome.tech
import hashlib
from aead import seal, open_sealed

GCM, AAD = "AES-256-GCM", b"orders.db"
def demo_key(label: str) -> bytes:   # stand-in for keys a KMS or HSM holds
    return hashlib.sha256(label.encode()).digest()

kek_v1, kek_v2 = demo_key("kek v1, demo"), demo_key("kek v2, demo")
dek = demo_key("dek for orders.db, demo")
n0, n1, n2 = (bytes(11) + bytes([i]) for i in range(3))  # never reused

row = seal(GCM, dek, n0, AAD, b"order 1042: deliver to 221B Baker St")
wrapped = seal(GCM, kek_v1, n1, AAD, dek)      # stored next to the data
print("row on disk:      ", row[0].hex()[:40] + "...")
print("DEK wrapped by v1:", wrapped[0].hex()[:40] + "...")

# rotate the KEK: unwrap with v1, wrap again with v2. The row is untouched.
plain = open_sealed(GCM, kek_v1, n1, AAD, *wrapped)
wrapped = seal(GCM, kek_v2, n2, AAD, plain)
print("DEK wrapped by v2:", wrapped[0].hex()[:40] + "...")
dek_now = open_sealed(GCM, kek_v2, n2, AAD, *wrapped)
print("row reads as:     ", open_sealed(GCM, dek_now, n0, AAD, *row).decode())
