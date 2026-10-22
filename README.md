\# Financial ML Model Security Audit



\## Overview

This project demonstrates a security audit of a machine-learning pipeline, focusing on unsafe model deserialization, hardcoded credentials, input validation, and custom Semgrep rules.



\## Objectives

\- Identify unsafe Python pickle deserialization.

\- Create and test custom Semgrep security rules.

\- Detect potential secrets and insecure model-loading patterns.

\- Document remediation recommendations.



\## Tools

\- Python

\- Semgrep

\- Git and GitHub



\## Project Structure

\- `rules/` — Custom Semgrep rules

\- `src/` — Remediated source code

\- `tests/` — Vulnerable test cases

\- `results/` — Scan evidence

\- `report/` — Security audit report



\## Current Test Evidence

A custom Semgrep rule successfully detected an unsafe `pickle.load()` call in a test Python file.



\## Limitations

Only the unsafe-pickle test has been confirmed so far. Full-project scans, additional custom rules, and remediation verification must be completed before claiming the audit is fully validated.



\## Security Note

The vulnerable examples are for educational testing only. Never commit real credentials, private keys, access tokens, or confidential data.



