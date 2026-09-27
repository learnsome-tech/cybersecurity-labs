# Cybersecurity Fundamentals, GRC & Cryptography — lesson m03l04 — Public Key Infrastructure: X.509 Certificates & CAs
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l04
# © LearnSome.tech
bash mkpki.sh > /dev/null 2>&1
: > index.txt
openssl ca -config ca.cnf -cert ca.pem -keyfile ca.key -revoke www.pem \
  -crl_reason keyCompromise 2>/dev/null

# the client asks about one serial number
openssl ocsp -issuer ca.pem -cert www.pem -no_nonce -reqout request.der
openssl ocsp -reqin request.der -req_text | grep -E 'Serial'

# the responder looks it up and signs an answer
openssl ocsp -index index.txt -CA ca.pem -rsigner ca.pem -rkey ca.key \
  -reqin request.der -respout response.der > /dev/null 2>&1
openssl ocsp -respin response.der -resp_text -noverify | grep 'Status:'

# the client checks the responder's signature and reads the status
openssl ocsp -respin response.der -issuer ca.pem -cert www.pem \
  -CAfile ca.pem -no_nonce 2>&1 | grep -E 'verify|www.pem|Reason'
