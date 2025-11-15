# 🧑‍🎓 Student Management System

A Python-based CLI tool to manage student records using JSON storage. Built for academic use, internship portfolios, and real-world learning.

---

## 🚀 Features

- Add, view, update, and delete student records
- Search students by name, ID, or grade
- List all students in a formatted table
- Export student data to CSV
- Admin login system (optional)
- JSON-based persistent storage
- Modular class structure with unit tests
- Reviewer-friendly CLI menu and demo script

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Option 1: CMD

```bash
cd "C:\Users\kavya rana\OneDrive\Desktop\StudentManagementSystem"
python student_management_system.py
```

### Option 2: Double-click

Run `run.bat` from the project folder

---

## 📁 Folder Structure

```
StudentManagementSystem/
├── student_management_system.py       # Main logic
├── students.json                      # Data file
├── requirements.txt                   # Dependencies
├── README.md                          # Project overview
├── run.bat                            # One-click launcher
├── demo_script.txt                    # Sample walkthrough
├── .gitignore                         # Git exclusions
│
├── screenshots/                       # GitHub visuals
├── utils/                             # Login system
│   └── auth.py
├── exports/                           # CSV exports
│   └── students.csv
└── tests/                             # Unit tests
    ├── test_student.py
    └── test_system.py
```

---

## 📸 Screenshots

### Project Folder
![Folder Structure](screenshots/folder_structure.png)

### CMD Execution
![Run in CMD](screenshots/cmd_run.png)

### JSON Data
![Student JSON](screenshots/json_data.png)

### List Students
![List Output](screenshots/list_students.png)

### Search Students
![Search Output](screenshots/search_output.png)

---

## 🎥 Demo Script

See `demo_script.txt` for full walkthrough:
- Add student
- View student
- List all students
- Search students
- Export to CSV
- Delete student
- Exit

---

## 🧪 Testing

Run unit tests:

```bash
python -m unittest tests/test_student.py
python -m unittest tests/test_system.py
```

---

## 🔐 Admin Login (Optional)

```python
from utils.auth import login

if not login():
    return
```

Default credentials:
- Username: `admin`
- Password: `1234`

---

## 📤 Export to CSV

```python
sms.export_to_csv()
```

File saved to: `exports/students.csv`

---

## 🙌 Author

**Kavya Rana**  
Roll No: BU2023UGBCA079  
Bahra University, Shimla Hills  
Mentor: Parul Ma’am

---

## 📘 License

This project is for academic and internship use. Free to modify and extend.