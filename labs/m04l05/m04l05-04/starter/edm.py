import csv, hashlib, re
from collections import defaultdict

def fp(value):
    return hashlib.sha256(value.strip(" .?").lower().encode()).hexdigest()

index = {}  # fingerprint -> (customer, field); the raw values are not kept
for row in csv.DictReader(open("customers.csv")):
    for field in ("email", "phone", "ni_number"):
        index[fp(row[field])] = (row["customer_id"], field)

for line in open("outgoing.txt"):
    channel, text = line.rstrip().split(": ", 1)
    hits = defaultdict(list)
    for token in re.split(r"[\s,;]+", text):
        if fp(token) in index:
            customer, field = index[fp(token)]
            hits[customer].append(field)
    worst = max(hits.values(), key=len, default=[])
    action = "block" if len(worst) >= 2 else "alert" if worst else "allow"
    print(f"{channel:<14} {action:<6}", dict(hits) or "no customer data")
