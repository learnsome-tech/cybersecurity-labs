# Cybersecurity Fundamentals, GRC & Cryptography — lesson m05l02 — Disaster Recovery Sites: Hot, Warm & Cold
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l02
# © LearnSome.tech
import sqlite3
from datetime import datetime, timedelta

def site():
    db = sqlite3.connect(":memory:")
    db.execute("create table orders (id integer primary key, at text)")
    return db

def ship(src, dst):                 # copy rows the replica has not seen
    seen = dst.execute("select coalesce(max(id), 0) from orders").fetchone()
    dst.executemany("insert into orders values (?, ?)", src.execute(
        "select * from orders where id > ?", seen))
primary, near, far = site(), site(), site()
t, fail = datetime(2026, 3, 9, 9, 0), datetime(2026, 3, 9, 14, 37)
while t < fail:                     # an order every two minutes
    primary.execute("insert into orders (at) values (?)", (t.isoformat(),))
    ship(primary, near)             # synchronous: before we say "paid"
    if t.minute % 15 == 0:
        ship(primary, far)          # asynchronous: every fifteen minutes
    t += timedelta(minutes=2)
for name, db in [("primary", primary), ("sync", near), ("async", far)]:
    print(name, db.execute("select count(*), max(at) from orders").fetchone())
