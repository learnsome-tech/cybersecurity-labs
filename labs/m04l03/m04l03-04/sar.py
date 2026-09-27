# Cybersecurity Fundamentals, GRC & Cryptography — lesson m04l03 — Privacy Principles, GDPR Subject Rights & Minimization
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l03
# © LearnSome.tech
import json, sqlite3
db = sqlite3.connect(":memory:")
db.executescript(open("shop.sql").read())
email = "alice@example.com"
cid, = db.execute("SELECT id FROM customers WHERE email=?", (email,)).fetchone()

export = {}
for (table,) in db.execute("SELECT name FROM sqlite_master WHERE type='table'"):
    cols = [c[1] for c in db.execute(f"PRAGMA table_info({table})")]
    key, value = ("email", email) if "email" in cols else ("customer_id", cid)
    rows = db.execute(f"SELECT * FROM {table} WHERE {key}=?", (value,))
    export[table] = [dict(zip(cols, r)) for r in rows]
    print(f"{table}: {len(export[table])} row(s) matched on {key}")

with open("alice-export.json", "w") as f:
    json.dump(export, f, indent=2)
print("wrote alice-export.json with", sum(map(len, export.values())), "records")
