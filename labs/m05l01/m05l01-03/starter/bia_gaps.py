import csv
from graphlib import TopologicalSorter

rows = {r["process"]: r for r in csv.DictReader(open("bia.csv"))}
deps = {p: set(filter(None, r["depends_on"].split(";")))
        for p, r in rows.items()}
ready = {}
for p in TopologicalSorter(deps).static_order():
    r = rows[p]
    rto = float(r["mtd_h"]) - float(r["wrt_h"])
    waits = max((ready[d] for d in deps[p]), default=0)
    ready[p] = waits + float(r["restore_h"])
    rpo, every = float(r["rpo_h"]), float(r["backup_every_h"])
    late = ready[p] - rto
    print(f"{p}: RTO {rto:g}h, ready after {ready[p]:g}h",
          "ok" if late <= 0 else f"late by {late:g}h")
    print(f"{p}: RPO {rpo:g}h, backup every {every:g}h",
          "ok" if every <= rpo else f"could lose {every:g}h of data")
