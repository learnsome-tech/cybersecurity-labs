from collections import defaultdict
fields, rows = [], []
for line in open("conn.log"):
    parts = line.rstrip("\n").split("\t")
    if parts[0] == "#fields":
        fields = parts[1:]
    elif not parts[0].startswith("#"):
        rows.append(dict(zip(fields, parts)))

def count(value):  # Zeek writes "-" for an unset field
    return 0 if value == "-" else int(value)

totals = defaultdict(lambda: [0, 0])  # (source, destination) -> sent, received
for r in rows:
    if r["local_orig"] == "T" and r["local_resp"] == "F":  # leaving the site
        pair = (r["id.orig_h"], r["id.resp_h"])
        totals[pair][0] += count(r["orig_bytes"])
        totals[pair][1] += count(r["resp_bytes"])
for (src, dst), (sent, received) in sorted(totals.items()):
    note = "review" if sent > 100e6 and sent > 10 * received else ""
    print(f"{src} -> {dst:<14} sent {sent / 1e6:7.1f} MB,"
          f" received {received / 1e6:6.1f} MB {note}")
