# Cybersecurity Fundamentals, GRC & Cryptography — lesson m04l03 — Privacy Principles, GDPR Subject Rights & Minimization
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l03
# © LearnSome.tech
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript(open("shop.sql").read())
TODAY = "2026-09-27"  # fixed so the output repeats; use date('now') for real
TABLES = ("customers", "orders", "marketing", "support_tickets")
def counts(step):
    n = [db.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in TABLES]
    print(f"{step:<10}", dict(zip(TABLES, n)))
counts("before")
# Erasure request from Alice (customer 1), identity verified. Orders stay: tax.
db.execute("DELETE FROM marketing WHERE customer_id=1")
db.execute("DELETE FROM support_tickets WHERE email='alice@example.com'")
db.execute("UPDATE customers SET email=NULL, name='erased' WHERE id=1")
counts("erasure")
# Storage limitation applies to everyone, request or not.
db.execute("DELETE FROM support_tickets WHERE closed < date(:d, '-2 years')",
           {"d": TODAY})
db.execute("DELETE FROM orders WHERE placed < date(:d, '-6 years')",
           {"d": TODAY})
counts("retention")
kept = db.execute("SELECT * FROM orders WHERE customer_id=1").fetchall()
print("alice's orders kept:", kept)
