# Cybersecurity Fundamentals, GRC & Cryptography — lesson m03l01 — Symmetric Encryption: AES-GCM & ChaCha20
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l01
# © LearnSome.tech
from aead import seal, open_sealed

KEY = bytes(range(32))
NONCE = bytes(12)  # the bug: a constant nonce, reused for every message
ALG = "ChaCha20-Poly1305"

known = b"status: all systems normal, no action"   # attacker guessed this
secret = b"new door code is 7713, change Friday"

c1, _ = seal(ALG, KEY, NONCE, b"", known)
c2, t2 = seal(ALG, KEY, NONCE, b"", secret)
opened = open_sealed(ALG, KEY, NONCE, b"", c2, t2)
print("message two still opens:", opened.decode())

keystream = bytes(c ^ p for c, p in zip(c1, known))
recovered = bytes(c ^ k for c, k in zip(c2, keystream))
print("recovered without the key:", recovered.decode())
