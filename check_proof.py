import sys

with open("proof.txt", "r") as f:
    content = f.read().lower()

errors = []

if "theorem" not in content:
    errors.append("Missing THEOREM section")

if "proof" not in content:
    errors.append("Missing PROOF section")

if "let" not in content:
    errors.append("Missing logical step (LET)")

if "then" not in content:
    errors.append("Missing logical step (THEN)")

if "so" not in content:
    errors.append("Missing conclusion (SO)")

if errors:
    print("Proof validation failed ❌")
    for e in errors:
        print("-", e)
    sys.exit(1)
else:
    print("Proof structure is valid ✅")
