set -e
printf 'firmware 7.1 for model A200\n' > firmware.txt
size() { wc -c < "$1" | tr -d ' '; }

for alg in ED25519 ML-DSA-65 SLH-DSA-SHA2-128s; do
  openssl genpkey -algorithm "$alg" -out "$alg.key"
  openssl pkey -in "$alg.key" -pubout -out "$alg.pub"
  openssl pkey -pubin -in "$alg.pub" -outform DER -out "$alg.der"
  openssl pkeyutl -sign -rawin -inkey "$alg.key" -in firmware.txt \
    -out "$alg.sig"
  openssl pkeyutl -verify -rawin -pubin -inkey "$alg.pub" -in firmware.txt \
    -sigfile "$alg.sig" > /dev/null && status="verifies"
  echo "$alg: public key $(size "$alg.der") bytes," \
    "signature $(size "$alg.sig") bytes, $status"
done
