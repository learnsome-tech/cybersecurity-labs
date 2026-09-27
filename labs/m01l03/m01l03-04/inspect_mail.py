# Cybersecurity Fundamentals, GRC & Cryptography — lesson m01l03 — Social Engineering, Phishing & Human Defense
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m01l03
# © LearnSome.tech
from email import policy
from email.parser import BytesParser
from email.utils import parseaddr

with open("invoice.eml", "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

name, address = parseaddr(msg["From"])
print("display name: ", name)
print("from address: ", address)
print("replies go to:", msg["Reply-To"])
print("bounces go to:", msg["Return-Path"])
for check in str(msg["Authentication-Results"]).split(";")[1:]:
    print("auth result:  ", check.strip())
