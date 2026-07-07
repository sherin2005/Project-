# Password Strength Analyzer (Educational Tool)

**Team No. 9 — Internship Project**
Amrita Vishwa Vidyapeetham, Kochi Campus
Internship at Unique Occassio Tech Pvt. Ltd. (UoTech), Kochi
Faculty Guide: Mahesh A. S., Assistant Professor, Dept. of Computer Science & IT

## Overview

A standalone Python CLI tool that evaluates the cryptographic strength of a
user-supplied password. It analyzes character composition, computes the total
theoretical keyspace, estimates brute-force crack time at a simulated attack
speed of 1,000,000 guesses/second, and classifies the result as **WEAK**,
**MEDIUM**, or **STRONG**.

This matches the design and requirements documented in the internship report
(Chapters 2–4): functional/non-functional requirements, system architecture,
interface design, and the QA test plan.

## How It Works

1. **Input** – the user types a password at the prompt.
2. **Length** – `len(password)` gives the string length.
3. **Charset evaluation** – four independent checks add to a running total:
   - lowercase letters present → +26
   - uppercase letters present → +26
   - digits present → +10
   - punctuation present → +32
4. **Validation** – if charset is 0 (empty input or unrecognized characters),
   the program prints `Invalid password` and exits safely.
5. **Combinatorics** – `combinations = charset ** length`
6. **Time estimate** – `seconds = combinations / 1,000,000`
7. **Classification**:
   - `< 60s` → WEAK
   - `60s – 86,400s` → MEDIUM
   - `≥ 86,400s` → STRONG

## Requirements

- Python 3.8+
- No external dependencies — uses only the standard library (`string`)

## Running the Tool

```bash
python3 code.py
```

Example session:

```
Password Strength Analyzer (Educational Tool)
Enter password to analyze: Str0ng!Pass

Analysis Result
Length: 11
Charset size: 94
Estimated crack time (seconds): 5062982072492057
Strength: STRONG
```

## Running the Test Suite

An automated test suite (`test_analyzer.py`) reproduces the manual test cases
from Chapter 4.2 of the report (TC01–TC08: input validation, unit tests,
boundary tests, and a stress test for large integers).

```bash
python3 -m unittest test_analyzer.py -v
```

All 8 test cases pass.

## Note on the Report's Test Case Table

While verifying this implementation against the report, two of the worked
examples in Chapter 4.2 have numeric typos:

| Password | Report says | Actual (verified) | Strength (still correct?) |
|---|---|---|---|
| `hello12` | crack time: 78 seconds | 78,364 seconds | MEDIUM — label is fine, seconds figure was rounded/typo'd |
| `test1234` | crack time: 2,821 seconds, **MEDIUM** | 2,821,109 seconds | **STRONG**, not MEDIUM — the report's classification is incorrect for this row |

This doesn't affect the tool's logic — the code itself is correct and
consistent with the described algorithm. If you're submitting the report
alongside this code, you may want to correct the `test1234` row in Chapter
4.2 (Strength should read STRONG) before final submission, since an examiner
who runs the actual script will get a different result than the table shows.

## File Structure

```
password_strength_analyzer/
├── code.py            # Main CLI application
├── test_analyzer.py   # Automated test suite (TC01–TC08)
└── README.md          # This file
```
