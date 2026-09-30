<p>
  <a href="https://learnsome.tech/courses/cybersecurity-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Cybersecurity Fundamentals, GRC & Cryptography

**Security Architecture, Risk Assessment, NIST CSF 2.0, AES/RSA PKI & Audit Readiness**

6 modules, 28 lessons: Core Security Principles; Governance, Risk & Compliance; Applied Cryptography & Keys; Data Protection & Privacy; Resilience & Disaster Recovery; Enterprise Strategy & Audit. Beginner level, about 3 hours.

This repository holds the labs of the LearnSome.tech course [Cybersecurity Fundamentals, GRC & Cryptography](https://learnsome.tech/courses/cybersecurity-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/cybersecurity-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7, SQLite 3.46.1, Git 2.34 (Ubuntu 22.04's) and OpenSSL 3.5, as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/cybersecurity-labs.git
  cd cybersecurity-labs
  ./check m01l01-02
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7, SQLite 3.46.1, Git 2.34 (Ubuntu 22.04's) and OpenSSL 3.5. Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-02`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Graded | Runs the program and compares its output with `expected.txt`. | 76 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 16 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: Core Security Principles

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [CIA Triad, Non-Repudiation & Parkerian Hexad](https://learnsome.tech/learn/cybersecurity-course/m01l01) | [3 labs](labs/m01l01/) | Free |
| 1.2 | [Threat Actors, Motivations & Cyber Kill Chain](https://learnsome.tech/learn/cybersecurity-course/m01l02) | [3 labs](labs/m01l02/) | Free |
| 1.3 | [Social Engineering, Phishing & Human Defense](https://learnsome.tech/learn/cybersecurity-course/m01l03) | [4 labs](labs/m01l03/) | Free |
| 1.4 | [Defense-in-Depth & Security Control Categories](https://learnsome.tech/learn/cybersecurity-course/m01l04) | [4 labs](labs/m01l04/) | Free |
| 1.5 | [Security Governance vs Security Management](https://learnsome.tech/learn/cybersecurity-course/m01l05) | [3 labs](labs/m01l05/) | Free |

### Module 2: Governance, Risk & Compliance

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [Security Baselines, Policies & Hardening Standards](https://learnsome.tech/learn/cybersecurity-course/m02l01) | [3 labs](labs/m02l01/) | Pro |
| 2.2 | [Risk Assessment: Qualitative vs Quantitative](https://learnsome.tech/learn/cybersecurity-course/m02l02) | [3 labs](labs/m02l02/) | Pro |
| 2.3 | [Security Frameworks: NIST CSF 2.0, ISO 27001 & CIS](https://learnsome.tech/learn/cybersecurity-course/m02l03) | [2 labs](labs/m02l03/) | Pro |
| 2.4 | [Regulatory Compliance: SOC 2, HIPAA, GDPR & PCI-DSS](https://learnsome.tech/learn/cybersecurity-course/m02l04) | [3 labs](labs/m02l04/) | Pro |
| 2.5 | [Vendor & Third-Party Risk Management Programs](https://learnsome.tech/learn/cybersecurity-course/m02l05) | [3 labs](labs/m02l05/) | Pro |

### Module 3: Applied Cryptography & Keys

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [Symmetric Encryption: AES-GCM & ChaCha20](https://learnsome.tech/learn/cybersecurity-course/m03l01) | [3 labs](labs/m03l01/) | Pro |
| 3.2 | [Asymmetric Cryptography: RSA, ECC & Diffie-Hellman](https://learnsome.tech/learn/cybersecurity-course/m03l02) | [3 labs](labs/m03l02/) | Pro |
| 3.3 | [Cryptographic Hashing: SHA-256, SHA-3 & Passwords](https://learnsome.tech/learn/cybersecurity-course/m03l03) | [4 labs](labs/m03l03/) | Pro |
| 3.4 | [Public Key Infrastructure: X.509 Certificates & CAs](https://learnsome.tech/learn/cybersecurity-course/m03l04) | [4 labs](labs/m03l04/) | Pro |
| 3.5 | [Post-Quantum Cryptography & Key Lifecycles](https://learnsome.tech/learn/cybersecurity-course/m03l05) | [3 labs](labs/m03l05/) | Pro |

### Module 4: Data Protection & Privacy

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [Data Classification Schemes & Sensitivity Labeling](https://learnsome.tech/learn/cybersecurity-course/m04l01) | [3 labs](labs/m04l01/) | Pro |
| 4.2 | [Data States: Security at Rest, in Transit, and in Use](https://learnsome.tech/learn/cybersecurity-course/m04l02) | [4 labs](labs/m04l02/) | Pro |
| 4.3 | [Privacy Principles, GDPR Subject Rights & Minimization](https://learnsome.tech/learn/cybersecurity-course/m04l03) | [3 labs](labs/m04l03/) | Pro |
| 4.4 | [Asset Lifecycle Management & Media Sanitization](https://learnsome.tech/learn/cybersecurity-course/m04l04) | [4 labs](labs/m04l04/) | Pro |
| 4.5 | [Data Loss Prevention & Egress Monitoring](https://learnsome.tech/learn/cybersecurity-course/m04l05) | [4 labs](labs/m04l05/) | Pro |

### Module 5: Resilience & Disaster Recovery

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [Business Impact Analysis, RTO & RPO Modeling](https://learnsome.tech/learn/cybersecurity-course/m05l01) | [4 labs](labs/m05l01/) | Pro |
| 5.2 | [Disaster Recovery Sites: Hot, Warm & Cold](https://learnsome.tech/learn/cybersecurity-course/m05l02) | [3 labs](labs/m05l02/) | Pro |
| 5.3 | [Backup Architectures: 3-2-1, Immutability & Air-Gaps](https://learnsome.tech/learn/cybersecurity-course/m05l03) | [4 labs](labs/m05l03/) | Pro |
| 5.4 | [Incident Roles, Escalation & Crisis Comm](https://learnsome.tech/learn/cybersecurity-course/m05l04) | [3 labs](labs/m05l04/) | Pro |

### Module 6: Enterprise Strategy & Audit

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 6.1 | [Security Architecture Gap Analysis](https://learnsome.tech/learn/cybersecurity-course/m06l01) | [3 labs](labs/m06l01/) | Pro |
| 6.2 | [Enterprise Risk Registers & Treatment Plans](https://learnsome.tech/learn/cybersecurity-course/m06l02) | [3 labs](labs/m06l02/) | Pro |
| 6.3 | [Internal Audits, Sampling & Evidence Chains](https://learnsome.tech/learn/cybersecurity-course/m06l03) | [4 labs](labs/m06l03/) | Pro |
| 6.4 | [Security Capstone Review & Certification](https://learnsome.tech/learn/cybersecurity-course/m06l04) | [2 labs](labs/m06l04/) | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
