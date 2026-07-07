"""
Password Strength Analyzer (Educational Tool)
-----------------------------------------------
Internship Project - Team No. 9
Amrita Vishwa Vidyapeetham, Kochi Campus

Evaluates password strength by analyzing character composition,
computing the theoretical keyspace, and estimating brute-force
crack time against a simulated attack speed of 1,000,000 guesses/sec.

Standard library only: string, math
"""

import string
import math


def analyze_password(password: str) -> None:
    """
    Runs the full analysis pipeline on a password:
    1. Length determination
    2. Character set (charset) evaluation
    3. Validation / error isolation
    4. Combinatorics (keyspace) calculation
    5. Brute-force time estimation
    6. Strength classification
    7. Output presentation
    """

    # ---- Step 3: Dimensional Metrics Computation ----
    length = len(password)

    # ---- Step 4: Character Set Parsing Engine ----
    charset = 0

    if any(ch.islower() for ch in password):
        charset += 26   # lowercase a-z

    if any(ch.isupper() for ch in password):
        charset += 26   # uppercase A-Z

    if any(ch.isdigit() for ch in password):
        charset += 10   # digits 0-9

    if any(ch in string.punctuation for ch in password):
        charset += 32   # standard punctuation/symbols

    # ---- Step 5: Error Isolation and Security Checkpoint ----
    if charset == 0:
        print("Invalid password")
        exit()

    # ---- Step 6: Combinatorics Permutation Calculations ----
    combinations = charset ** length

    # ---- Step 7: Brute-Force Time Emulation ----
    guesses_per_sec = 1_000_000
    seconds = combinations / guesses_per_sec

    # ---- Step 8: Security Classification Routing ----
    if seconds < 60:
        strength = "WEAK"
    elif seconds < 86_400:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    # ---- Step 9: Output Presentation ----
    print("\nAnalysis Result")
    print(f"Length: {length}")
    print(f"Charset size: {charset}")
    print(f"Estimated crack time (seconds): {int(seconds)}")
    print(f"Strength: {strength}")


def main():
    print("Password Strength Analyzer (Educational Tool)")
    password = input("Enter password to analyze: ")
    analyze_password(password)


if __name__ == "__main__":
    main()
