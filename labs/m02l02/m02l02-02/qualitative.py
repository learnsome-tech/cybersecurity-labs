# Cybersecurity Fundamentals, GRC & Cryptography — lesson m02l02 — Risk Assessment: Qualitative vs Quantitative
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l02
# © LearnSome.tech
import csv

APPETITE = 9  # board-approved: scores above this need a treatment plan

def band(score):
    if score >= 15:
        return "critical"
    if score >= 10:
        return "high"
    return "medium" if score >= 5 else "low"

with open("register.csv", newline="") as f:
    rows = list(csv.DictReader(f))
for r in rows:
    r["score"] = int(r["likelihood"]) * int(r["impact"])

for r in sorted(rows, key=lambda r: -r["score"]):
    s = r["score"]
    action = "treat" if s > APPETITE else "accept"
    print(f'{r["id"]} {s:2} {band(s):8} {action:6} {r["risk"]}')
