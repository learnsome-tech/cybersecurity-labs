# Cybersecurity Fundamentals, GRC & Cryptography — lesson m04l05 — Data Loss Prevention & Egress Monitoring
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l05
# © LearnSome.tech
import re
CANDIDATE = re.compile(r"\b\d(?:[ -]?\d){12,18}\b")  # 13 to 19 digits

def luhn_ok(digits):
    total = 0
    for i, ch in enumerate(reversed(digits)):
        d = int(ch)
        if i % 2 == 1:  # double every second digit from the right
            d = d * 2 - 9 if d > 4 else d * 2
        total += d
    return total % 10 == 0

body = open("outbound.eml").read().split("\n\n", 1)[1]  # skip the headers
for match in CANDIDATE.finditer(body):
    digits = re.sub(r"\D", "", match.group())
    verdict = "card number" if luhn_ok(digits) else "fails Luhn, not a card"
    print(f"{match.group():<22} {verdict}")
