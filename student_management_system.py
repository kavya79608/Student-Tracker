# student_management_system.py

import json
import os
from datetime import datetime
from utils.auth import login

class Student:
    def __init__(self, student_id, name, age, grade, subjects=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects if subjects else []
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "subjects": self.subjects,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        student = Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["grade"],
            data.get("subjects", [])
        )
        student.created_at = data.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return student

class StudentManagementSystem:
    def __init__(self, data_file="students.json"):
        self.data_file = data_file
        self.students = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                for student_id, student_data in data.items():
                    self.students[student_id] = Student.from_dict(student_data)

    def save_data(self):
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump({sid: s.to_dict() for sid, s in self.students.items()}, file, indent=4)

    def add_student(self, student_id, name, age, grade, subjects):
        if student_id in self.students:
            return False, "Student with this ID already exists"
        student = Student(student_id, name, age, grade, subjects)
        self.students[student_id] = student
        self.save_data()
        return True, "Student added successfully"

    def get_student(self, student_id):
        return self.students.get(student_id)

    def update_student(self, student_id, name=None, age=None, grade=None, subjects=None):
        student = self.get_student(student_id)
        if not student:
            return False, "Student not found"
        if name: student.name = name
        if age: student.age = age
        if grade: student.grade = grade
        if subjects: student.subjects = subjects
        self.save_data()
        return True, "Student updated successfully"

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            return True, "Student deleted successfully"
        return False, "Student not found"

    def list_students(self):
        return list(self.students.values())

    def search_students(self, term):
        term = term.lower()
        return [s for s in self.students.values()
                if term in s.name.lower() or term in s.student_id.lower() or term in s.grade.lower()]

    def export_to_csv(self, filename="exports/students.csv"):
        import csv
        os.makedirs("exports", exist_ok=True)
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Age", "Grade", "Subjects", "Created At"])
            for student in self.students.values():
                writer.writerow([
                    student.student_id,
                    student.name,
                    student.age,
                    student.grade,
                    ', '.join(student.subjects),
                    student.created_at
                ])
        return True, f"Student data exported to {filename}"

def main():
    sms = StudentManagementSystem()

    if not login():
        return

    while True:
        print("\n📚 Student Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. List All Students")
        print("6. Search Students")
        print("7. Exit")
        print("8. Export to CSV")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = input("Enter Student Grade: ")
            subjects = input("Enter Subjects (comma separated, optional): ").split(",")
            subjects = [s.strip() for s in subjects if s.strip()]
            success, message = sms.add_student(student_id, name, age, grade, subjects)
            print(message)

        elif choice == '2':
            student_id = input("Enter Student ID to view: ")
            student = sms.get_student(student_id)
            if student:
                print("\n📋 Student Details:")
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
                print(f"Subjects: {', '.join(student.subjects)}")
                print(f"Created At: {student.created_at}")
            else:
                print("❌ Student not found")

        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            name = input("New Name (leave blank to skip): ")
            age = input("New Age (leave blank to skip): ")
            grade = input("New Grade (leave blank to skip): ")
            subjects = input("New Subjects (comma separated, leave blank to skip): ")
            age = int(age) if age else None
            subjects = [s.strip() for s in subjects.split(",")] if subjects else None
            success, message = sms.update_student(student_id, name or None, age, grade or None, subjects)
            print(message)

        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            confirm = input(f"Are you sure you want to delete student {student_id}? (y/n): ")
            if confirm.lower() == 'y':
                success, message = sms.delete_student(student_id)
                print(message)

        elif choice == '5':
            students = sms.list_students()
            if students:
                print("\n📊 All Students:")
                print(f"{'ID':<12} {'Name':<20} {'Age':<5} {'Grade':<10} {'Subjects'}")
                print("-" * 60)
                for s in students:
                    print(f"{s.student_id:<12} {s.name:<20} {s.age:<5} {s.grade:<10} {', '.join(s.subjects)}")
            else:
                print("No students found.")

        elif choice == '6':
            term = input("Enter search term (name, ID, or grade): ")
            results = sms.search_students(term)
            if results:
                print(f"\n📊 Search Results for '{term}':")
                print(f"{'ID':<12} {'Name':<20} {'Age':<5} {'Grade':<10} {'Subjects'}")
                print("-" * 60)
                for s in results:
                    print(f"{s.student_id:<12} {s.name:<20} {s.age:<5} {s.grade:<10} {', '.join(s.subjects)}")
            else:
                print("No matching students found.")

        elif choice == '8':
            success, message = sms.export_to_csv()
            print(message)

        elif choice == '7':
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()