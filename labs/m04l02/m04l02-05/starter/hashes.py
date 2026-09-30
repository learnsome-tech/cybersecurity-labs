import datetime, hashlib, hmac
KEY = b"FAKE-demo-key-kept-in-a-key-manager"  # never shipped with the data

def sha(value):
    return hashlib.sha256(value.encode()).hexdigest()

def keyed(value):
    return hmac.new(KEY, value.encode(), "sha256").hexdigest()

def guess(target, fn):  # try every birth date from 1920 to 2010
    day, tries = datetime.date(1920, 1, 1), 0
    while day.year <= 2010:
        tries += 1
        if fn(day.isoformat()) == target:
            return f"recovered {day} after {tries} guesses"
        day += datetime.timedelta(days=1)
    return f"no match after {tries} guesses"

print("plain SHA-256:", guess(sha("1987-03-14"), sha))
print("HMAC, key unknown:", guess(keyed("1987-03-14"), sha))
