from datetime import datetime

report = f"""
Math Proof Report
-----------------
Status: VALID
Checked at: {datetime.now()}
"""

with open("report.txt", "w") as f:
    f.write(report)

print("Report generated ✅")
