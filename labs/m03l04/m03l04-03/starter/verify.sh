bash mkpki.sh > /dev/null 2>&1   # the CA and www.pem from the last script
OCT_1=1790812800                 # 2026-10-01, inside the validity period
JAN_1=1798761600                 # 2027-01-01, after notAfter

check() {  # a label, then extra arguments for openssl verify
  label=$1; shift
  result=$(openssl verify -CAfile ca.pem "$@" 2>&1 | grep -E ': OK$|lookup:')
  printf "%-13s %s\n" "$label" "${result#*lookup: }"
}

# an attacker's certificate for the same name, signed by its own key
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:P-256 -noenc -quiet \
  -keyout fake.key -out fake.pem -subj "/CN=www.example.com" 2>/dev/null

check "right name:" -attime $OCT_1 -verify_hostname www.example.com www.pem
check "wrong name:" -attime $OCT_1 -verify_hostname shop.example.com www.pem
check "after expiry:" -attime $JAN_1 www.pem
check "self-signed:" -attime $OCT_1 fake.pem
