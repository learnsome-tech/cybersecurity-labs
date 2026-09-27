# Cybersecurity Fundamentals, GRC & Cryptography — lesson m02l03 — Security Frameworks: NIST CSF 2.0, ISO 27001 & CIS
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l03
# © LearnSome.tech
import csv
from datetime import date

AUDIT_DAY, MAX_AGE = date(2026, 3, 31), 365  # older evidence is rejected

controls = list(csv.DictReader(open("crosswalk.csv")))
evidence = {e["csf"]: e for e in csv.DictReader(open("evidence.csv"))}

def status(csf_id):
    if csf_id not in evidence:
        return "no evidence"
    age = AUDIT_DAY - date.fromisoformat(evidence[csf_id]["collected"])
    return "ok" if age.days <= MAX_AGE else "evidence too old"

score = {}
for c in controls:
    s, fn = status(c["csf"]), c["csf"][:2]
    ok, total = score.get(fn, (0, 0))
    score[fn] = (ok + (s == "ok"), total + 1)
    if s != "ok":
        print(f"{c['csf']:9} {s:16} ISO A.{c['iso27001']:5} CIS {c['cis_v8']}")
print("  ".join(f"{fn} {ok}/{n}" for fn, (ok, n) in score.items()))
