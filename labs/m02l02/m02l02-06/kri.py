# Cybersecurity Fundamentals, GRC & Cryptography — lesson m02l02 — Risk Assessment: Qualitative vs Quantitative
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l02
# © LearnSome.tech
import csv
from datetime import date, timedelta

GRACE = timedelta(days=14)  # standard: critical patches within 14 days
AMBER, RED = 10, 20         # per cent of hosts; red is the tolerance line

rows = list(csv.DictReader(open("internet_facing_patches.csv")))
hosts = {r["host"] for r in rows}

def overdue(r, on):
    released = date.fromisoformat(r["released"])
    done = r["installed"] and date.fromisoformat(r["installed"]) <= on
    return released + GRACE < on and not done

for month_end in ["2026-01-31", "2026-02-28", "2026-03-31"]:
    on = date.fromisoformat(month_end)
    late = sorted({r["host"] for r in rows if overdue(r, on)})
    pct = 100 * len(late) / len(hosts)
    status = "red" if pct >= RED else "amber" if pct >= AMBER else "green"
    print(f"{month_end} {pct:3.0f}% {status:5} {' '.join(late)}")
