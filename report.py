import csv
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.csv")

def generate_report():
    print("\n--- Student Report ---")
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        print("No student records found. Register a student first.")
        return

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("No student records found.")
        return

    print(f"{'Roll No':<12} {'Name':<22} {'Department':<18} {'Marks':>8} {'Result':>10}")
    print("-" * 75)
    for row in rows:
        try:
            marks = float(row["Marks"])
            result = "PASS" if marks >= 40 else "FAIL"
        except (ValueError, TypeError):
            marks, result = 0, "UNKNOWN"
        print(f"{row['Roll No']:<12} {row['Name']:<22} {row['Department']:<18} {marks:>8.1f} {result:>10}")

    average = sum(float(row["Marks"]) for row in rows) / len(rows)
    print("-" * 75)
    print(f"Total students: {len(rows)}")
    print(f"Class average: {average:.2f}")

if __name__ == "__main__":
    generate_report()
