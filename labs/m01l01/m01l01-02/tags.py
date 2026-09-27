# Cybersecurity Fundamentals, GRC & Cryptography — lesson m01l01 — CIA Triad, Non-Repudiation & Parkerian Hexad
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m01l01
# © LearnSome.tech
import hashlib
import hmac

order = b"pay 1200.00 GBP to account 40300021"
forged = b"pay 1200.00 GBP to account 99887766"

# A plain hash travels with the message, so an attacker swaps both
sent_msg, sent_hash = forged, hashlib.sha256(forged).hexdigest()
print("sha256 matches forged order:",
      hashlib.sha256(sent_msg).hexdigest() == sent_hash)

KEY = bytes(range(32))  # demo key: the sender and the bank both hold it

def verify(msg, tag):
    good = hmac.new(KEY, msg, "sha256").hexdigest()
    return hmac.compare_digest(good, tag)

attacker_tag = hmac.new(b"guessed key", forged, "sha256").hexdigest()
print("hmac accepts attacker's tag:", verify(forged, attacker_tag))
bank_tag = hmac.new(KEY, forged, "sha256").hexdigest()
print("hmac accepts bank's own tag:", verify(forged, bank_tag))
