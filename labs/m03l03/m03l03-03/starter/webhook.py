import hashlib
import hmac

SECRET = b"demo-webhook-secret-not-real"   # shared by sender and receiver
body = b'{"order": 1042, "status": "paid", "amount": "49.00"}'
header = "sha256=" + hmac.new(SECRET, body, hashlib.sha256).hexdigest()


def plain_check(body: bytes, header: str) -> bool:   # the mistake
    return header == "sha256=" + hashlib.sha256(body).hexdigest()


def hmac_check(body: bytes, header: str) -> bool:
    good = "sha256=" + hmac.new(SECRET, body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(good, header)       # constant-time compare


forged = body.replace(b'"49.00"', b'"0.01"')
forged_header = "sha256=" + hashlib.sha256(forged).hexdigest()
print("genuine request, HMAC check:  ", hmac_check(body, header))
print("forged request, plain check:  ", plain_check(forged, forged_header))
print("forged request, HMAC check:   ", hmac_check(forged, forged_header))
