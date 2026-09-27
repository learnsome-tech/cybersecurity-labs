# Cybersecurity Fundamentals, GRC & Cryptography — lesson m02l04 — Regulatory Compliance: SOC 2, HIPAA, GDPR & PCI-DSS
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l04
# © LearnSome.tech
import hashlib, hmac

pan = "4111111111111111"  # a public test card number
stored_hash = hashlib.sha256(pan.encode()).hexdigest()
stored_masked = pan[:6] + "******" + pan[-4:]  # kept for display

head, tail = stored_masked[:6], stored_masked[-4:]
for middle in range(10**6):  # the attacker only lacks six digits
    guess = f"{head}{middle:06d}{tail}"
    if hashlib.sha256(guess.encode()).hexdigest() == stored_hash:
        print(f"plain SHA-256: recovered {guess} after {middle + 1:,} guesses")
        break

real_key = bytes(range(32))  # stand-in; the real key sits in a KMS or HSM
stored_mac = hmac.new(real_key, pan.encode(), "sha256").hexdigest()
wrong_key = b"attacker has no key".ljust(32, b"\0")
hits = sum(hmac.new(wrong_key, f"{head}{m:06d}{tail}".encode(), "sha256")
           .hexdigest() == stored_mac for m in range(10**6))
print(f"keyed HMAC-SHA-256: {hits} matches in 1,000,000 guesses")
