import csv
from datetime import datetime

rows = list(csv.DictReader(open("results.csv")))
sent = datetime.fromisoformat(rows[0]["sent"])

for field in ("clicked", "submitted", "reported"):
    count = sum(1 for r in rows if r[field])
    print(f"{field:<10} {count} of {len(rows)}")

reports = sorted(r["reported"] for r in rows if r["reported"])
first = datetime.fromisoformat(reports[0]) - sent
print("first report arrived", first, "after sending")
owned_up = [r["user"] for r in rows if r["clicked"] and r["reported"]]
print("clicked, then reported it:", ", ".join(owned_up))
