#!/usr/bin/env bash
# Cybersecurity Fundamentals, GRC & Cryptography — lesson m06l04 — Security Capstone Review & Certification
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m06l04
# © LearnSome.tech
# Evidence from the booking team: the certificate on booking.example.org
openssl x509 -in cert.pem -noout -subject -issuer -dates -ext subjectAltName \
  | sed 's/^ *//'
openssl x509 -in cert.pem -noout -text \
  | grep -E 'Public-Key|Signature Algorithm' | sed 's/^ *//' | sort -u
sha256sum cert.pem
