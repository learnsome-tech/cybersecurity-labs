# Cybersecurity Fundamentals, GRC & Cryptography — lesson m01l05 — Security Governance vs Security Management
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m01l05
# © LearnSome.tech
import csv
from datetime import date

AS_OF = date(2026, 9, 27)  # fixed, so the report can be reproduced
MAY_ACCEPT = {"low": {"IT manager", "CISO"}, "medium": {"CISO"},
              "high": {"CISO", "risk committee"}}

for ex in csv.DictReader(open("exceptions.csv")):
    issues = []
    if not ex["approved_by"]:
        issues.append("nobody approved it")
    elif ex["approved_by"] not in MAY_ACCEPT[ex["risk"]]:
        issues.append(f"{ex['approved_by']} cannot accept {ex['risk']} risk")
    expires = date.fromisoformat(ex["expires"])
    if expires < AS_OF:
        issues.append(f"expired on {expires}")
    elif (expires - AS_OF).days > 365:
        issues.append("longer than the one year maximum")
    print(f"{ex['id']} {ex['system']:<15}", "; ".join(issues) or "ok")
