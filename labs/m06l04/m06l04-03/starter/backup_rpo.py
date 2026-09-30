import json
from datetime import datetime, timedelta

RPO = timedelta(hours=24)                # from the business impact analysis
AUDIT = datetime.fromisoformat("2026-09-30T09:00:00+00:00")

snaps = json.load(open("snapshots.json"))  # saved from restic snapshots --json
times = sorted(datetime.fromisoformat(s["time"]).replace(second=0,
                                                          microsecond=0)
               for s in snaps)
times.append(AUDIT)                      # data written since the last backup

print("snapshots:", len(snaps), "from", times[0].date(), "to", times[-2].date())
for older, newer in zip(times, times[1:]):
    if newer - older > RPO:
        print(f"{older:%Y-%m-%d %H:%M} to {newer:%Y-%m-%d %H:%M}:",
              newer - older)

worst = max(newer - older for older, newer in zip(times, times[1:]))
print("worst case data loss:", worst, "against an RPO of", RPO)
print("PR.DS-11 backups:", "met" if worst <= RPO else "gap")
