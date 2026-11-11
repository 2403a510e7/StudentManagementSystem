import csv
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.csv")
FIELDS = ["Roll No", "Name", "Department", "Marks"]

def register_student():
    print("\n--- Student Registration ---")
    roll_no = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()
    department = input("Enter department: ").strip()
    marks_text = input("Enter marks (0-100): ").strip()

    if not all([roll_no, name, department, marks_text]):
        print("All fields are required.")
        return

    try:
        marks = float(marks_text)
        if not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        print("Marks must be a number between 0 and 100.")
        return

    existing_rolls = set()
    if DATA_FILE.exists():
        with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                existing_rolls.add(row["Roll No"])

    if roll_no in existing_rolls:
        print("A student with this roll number already exists.")
        return

    file_exists = DATA_FILE.exists()
    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if not file_exists or DATA_FILE.stat().st_size == 0:
            writer.writeheader()
        writer.writerow({
            "Roll No": roll_no,
            "Name": name,
            "Department": department,
            "Marks": f"{marks:g}"
        })

    print("Student registered successfully!")

if __name__ == "__main__":
    register_student()
