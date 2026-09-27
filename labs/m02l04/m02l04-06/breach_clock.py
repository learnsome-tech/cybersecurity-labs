# Cybersecurity Fundamentals, GRC & Cryptography — lesson m02l04 — Regulatory Compliance: SOC 2, HIPAA, GDPR & PCI-DSS
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l04
# © LearnSome.tech
from datetime import date, datetime, timedelta

aware = datetime.fromisoformat("2026-05-14T16:20+00:00")  # breach confirmed
affected = {"EU": 3400, "US-CA": 620, "US-TX": 140}
us_total = sum(n for where, n in affected.items() if where.startswith("US"))

print("GDPR supervisory authority by", aware + timedelta(hours=72))
print("HIPAA individuals no later than", (aware + timedelta(days=60)).date())
if us_total >= 500:
    print(f"HIPAA HHS Secretary: same deadline, {us_total} individuals")
else:
    year_end = date(aware.year, 12, 31)
    print("HIPAA HHS Secretary: annual log by", year_end + timedelta(days=60))
for where, n in affected.items():
    if where.startswith("US") and n > 500:
        print(f"HIPAA media notice in {where[3:]}: {n} residents")
