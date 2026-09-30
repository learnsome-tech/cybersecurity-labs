import re

# 13 to 19 digits, optionally separated by single spaces or dashes
CANDIDATE = re.compile(r"\b(?:\d[ -]?){12,18}\d\b")

def luhn_ok(digits):
    total = 0
    for i, d in enumerate(reversed(digits)):
        n = int(d) * (2 if i % 2 else 1)
        total += n - 9 if n > 9 else n
    return total % 10 == 0

for lineno, line in enumerate(open("support_export.log"), start=1):
    for m in CANDIDATE.finditer(line):
        digits = re.sub(r"\D", "", m.group())
        masked = digits[:6] + "*" * (len(digits) - 10) + digits[-4:]
        verdict = "card number" if luhn_ok(digits) else "fails Luhn, not a card"
        print(f"line {lineno}: {masked}  {verdict}")
