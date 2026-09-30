openssl genpkey -algorithm ed25519 -out alice.key
openssl pkey -in alice.key -pubout -out alice.pub

printf 'pay 1200.00 GBP to account 40300021\n' > order.txt
openssl pkeyutl -sign -rawin -inkey alice.key \
  -in order.txt -out order.sig

echo "bank checks the order Alice signed:"
openssl pkeyutl -verify -rawin -pubin -inkey alice.pub \
  -in order.txt -sigfile order.sig

echo "bank edits the account number and checks again:"
printf 'pay 1200.00 GBP to account 99887766\n' > order.txt
openssl pkeyutl -verify -rawin -pubin -inkey alice.pub \
  -in order.txt -sigfile order.sig 2>/dev/null
