# Cybersecurity Fundamentals, GRC & Cryptography — lesson m03l01 — Symmetric Encryption: AES-GCM & ChaCha20
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l01
# © LearnSome.tech
from aead import seal, open_sealed

KEY = bytes(range(32))         # same demo key as the counter mode program
NONCE = bytes(12)              # used once with this key, never again
header = b"invoice 2026-0042"  # sent in the clear, but still authenticated

sent, tag = seal("AES-256-GCM", KEY, NONCE, header,
                 b"pay 0100.00 GBP to 12345678")
print("on the wire:", sent.hex())
print("tag:        ", tag.hex())

tampered = bytearray(sent)
tampered[4] ^= ord("0") ^ ord("9")
for label, body in [("original", sent), ("tampered", bytes(tampered))]:
    try:
        plain = open_sealed("AES-256-GCM", KEY, NONCE, header, body, tag)
        print(f"{label}: {plain.decode()}")
    except ValueError as err:
        print(f"{label}: rejected, {err}")
