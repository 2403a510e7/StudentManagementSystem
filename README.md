# Student Management System

A beginner-friendly Python command-line application demonstrating Git and GitHub branching, commits, pushing, and pull-request merging.

## Features
- Student registration (roll number, name, department, marks)
- CSV-based local storage (`students.csv` is created automatically)
- Student report with PASS/FAIL status and class average
- Duplicate roll-number and marks validation

## Requirements
- Python 3.8 or later
- Git
- A GitHub account

No third-party Python packages are required.

## Run the project
```bash
python main.py
```

## Suggested GitHub collaboration workflow

The assignment requires two separate feature branches:

1. `student-registration` — contains `registration.py`
2. `student-report` — contains `report.py`

Create and push the branches separately, then merge each into `main` using a GitHub Pull Request.

### Initial setup
```bash
git init
git add main.py README.md
git commit -m "Initial project setup"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/StudentManagementSystem.git
git push -u origin main
```

### Feature branch 1: Student registration
```bash
git switch -c student-registration
git add registration.py
git commit -m "Add student registration feature"
git push -u origin student-registration
```
On GitHub, open a Pull Request with **base: `main`** and **compare: `student-registration`**, then merge it.

### Feature branch 2: Student report
Start from the updated main branch:
```bash
git switch main
git pull origin main
git switch -c student-report
git add report.py
git commit -m "Add student report generation feature"
git push -u origin student-report
```
On GitHub, open a Pull Request with **base: `main`** and **compare: `student-report`**, then merge it.

### Finish
```bash
git switch main
git pull origin main
git add main.py
git commit -m "Integrate student management features"
git push origin main
```

Check branches and history:
```bash
git branch -a
git log --oneline --graph --all
```

## Notes
- `students.csv` is generated when the first student is registered; it is intentionally not included in the repository.
- For a classroom demonstration, use sample student data only.
