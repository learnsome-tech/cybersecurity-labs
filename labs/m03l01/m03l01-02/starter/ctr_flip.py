import subprocess

KEY = bytes(range(32)).hex()   # demo key, shown in class on purpose
IV = "00" * 12 + "00000002"    # twelve byte nonce, then a block counter


def aes_ctr(data: bytes) -> bytes:
    cmd = ["openssl", "enc", "-aes-256-ctr", "-K", KEY, "-iv", IV]
    return subprocess.run(cmd, input=data, capture_output=True).stdout


order = b"pay 0100.00 GBP to 12345678"
sent = aes_ctr(order)
print("on the wire:", sent.hex())

tampered = bytearray(sent)
tampered[4] ^= ord("0") ^ ord("9")  # attacker knows the format, not the key
print("bank reads: ", aes_ctr(bytes(tampered)).decode())
