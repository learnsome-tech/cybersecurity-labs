import csv
from datetime import date

APPETITE = 8
REVIEW = date(2026, 9, 30)                  # date of the risk committee
LIMIT = {"ciso": 15, "cfo": 25, "ceo": 25}  # anyone else: up to appetite

for r in csv.DictReader(open("register.csv")):
    residual = int(r["rL"]) * int(r["rI"])
    when = date.fromisoformat(r["date"])
    if r["treatment"] in ("accept", "transfer"):
        allowed = LIMIT.get(r["approver"], APPETITE)
        if residual > allowed:
            print(f"{r['id']} signed by {r['approver']}, who may accept up "
                  f"to {allowed}; residual is {residual}")
        if when < REVIEW:
            print(f"{r['id']} sign-off expired on {when}")
    if r["treatment"] == "mitigate" and r["status"] != "done" \
            and when < REVIEW:
        print(f"{r['id']} action overdue since {when}, owner {r['owner']}")
