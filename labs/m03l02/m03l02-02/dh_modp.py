# Cybersecurity Fundamentals, GRC & Cryptography — lesson m03l02 — Asymmetric Cryptography: RSA, ECC & Diffie-Hellman
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l02
# © LearnSome.tech
import random
from modp2048 import P, G   # RFC 3526 group 14: public, the same for everyone

rng = random.Random(2026)  # fixed seed so the demo repeats;
a = rng.getrandbits(256)   # real code draws private values from secrets
b = rng.getrandbits(256)

A = pow(G, a, P)           # Alice sends this in the clear
B = pow(G, b, P)           # Bob sends this in the clear
print("prime:", P.bit_length(), "bits")
print("Alice sends:", hex(A)[:26] + "...")
print("Bob sends:  ", hex(B)[:26] + "...")

alice_secret = pow(B, a, P)  # Bob's public value, Alice's private one
bob_secret = pow(A, b, P)    # Alice's public value, Bob's private one
print("Alice gets: ", hex(alice_secret)[:26] + "...")
print("Bob gets:   ", hex(bob_secret)[:26] + "...")
print("same secret:", alice_secret == bob_secret)
