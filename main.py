from registration import register_student
from report import generate_report

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register Student")
        print("2. Generate Student Report")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
