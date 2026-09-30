import unicodedata

OURS = "example.com"
SEEN = ["example.com", "еxample.com", "examp1e.com", "exarnple.com",
        "example-invoices.com"]

def distance(a, b):
    row = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        prev, row[0] = row[0], i
        for j, cb in enumerate(b, 1):
            prev, row[j] = row[j], min(row[j] + 1, row[j - 1] + 1,
                                       prev + (ca != cb))
    return row[-1]

for domain in SEEN:
    wire = domain.encode("idna").decode()
    odd = [unicodedata.name(c) for c in domain if not c.isascii()]
    print(f"{wire:<21} edits: {distance(domain, OURS):<2}", *odd)
