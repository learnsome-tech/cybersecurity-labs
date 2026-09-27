# Cybersecurity Fundamentals, GRC & Cryptography — lesson m03l04 — Public Key Infrastructure: X.509 Certificates & CAs
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l04
# © LearnSome.tech
bash mkpki.sh > /dev/null 2>&1   # the CA and www.pem again
: > index.txt                    # the CA's database, named in ca.cnf

# the server key leaked: the CA marks serial 1000 revoked
openssl ca -config ca.cnf -cert ca.pem -keyfile ca.key -revoke www.pem \
  -crl_reason keyCompromise 2>/dev/null

# publish a signed list of revoked serial numbers, valid for one week
openssl ca -config ca.cnf -cert ca.pem -keyfile ca.key -gencrl -out crl.pem \
  -crl_lastupdate 20261010000000Z -crl_nextupdate 20261017000000Z 2>/dev/null
openssl crl -in crl.pem -noout -text | grep -E 'Update|Serial|Compromise'

OCT_12=1791763200                # 2026-10-12, inside the CRL's week
echo "without the CRL: $(openssl verify -CAfile ca.pem -attime $OCT_12 www.pem)"
openssl verify -CAfile ca.pem -crl_check -CRLfile crl.pem -attime $OCT_12 \
  www.pem 2>&1 | grep lookup
