set -e
# the CA: a key pair and a self-signed root certificate
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out ca.key
openssl req -x509 -key ca.key -out ca.pem -set_serial 1 \
  -subj "/O=Example Corp/CN=Example Corp Root CA" \
  -not_before 20260101000000Z -not_after 20360101000000Z \
  -addext "basicConstraints=critical,CA:TRUE"
# the server: its own key pair and a certificate signing request
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out www.key
openssl req -new -key www.key -out www.csr -subj "/CN=www.example.com" \
  -addext "subjectAltName=DNS:www.example.com,DNS:example.com"
# the CA checks the request's signature, then signs a certificate
openssl x509 -req -in www.csr -CA ca.pem -CAkey ca.key -out www.pem \
  -copy_extensions copy -set_serial 4096 \
  -not_before 20260901000000Z -not_after 20261130000000Z
openssl x509 -in www.pem -noout -issuer -subject -serial -dates \
  -ext subjectAltName
