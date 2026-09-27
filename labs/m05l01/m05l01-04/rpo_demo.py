# Cybersecurity Fundamentals, GRC & Cryptography — lesson m05l01 — Business Impact Analysis, RTO & RPO Modeling
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l01
# © LearnSome.tech
import sqlite3
from datetime import datetime, timedelta

EVERY = timedelta(hours=4)             # backup schedule
FAIL = datetime(2026, 3, 9, 5, 37)     # the disk controller dies
live = sqlite3.connect(":memory:")
live.execute("create table orders (id integer primary key, placed text)")
copy = sqlite3.connect(":memory:")
t = midnight = datetime(2026, 3, 9)
while t < FAIL:                        # an order every three minutes
    if (t - midnight) % EVERY == timedelta(0):
        live.commit()
        live.backup(copy)              # SQLite online backup API
        last = t
    live.execute("insert into orders (placed) values (?)", (t.isoformat(),))
    t += timedelta(minutes=3)
q = "select count(*), max(placed) from orders"
made = live.execute(q).fetchone()[0]
kept, newest = copy.execute(q).fetchone()
print(f"last backup {last:%H:%M}, failure {FAIL:%H:%M}, gap {FAIL - last}")
print(f"orders taken {made}, in the backup {kept}, newest {newest[11:16]}")
print(f"orders that exist nowhere now: {made - kept}")
