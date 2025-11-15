import unittest
from student_management_system import Student, StudentManagementSystem

class TestStudent(unittest.TestCase):

    def test_student_creation(self):
        student = Student("S001", "Kavya", 20, "Male", ["Python", "DBMS"])
        self.assertEqual(student.student_id, "S001")
        self.assertEqual(student.name, "Kavya")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.grade, "Male")
        self.assertIn("Python", student.subjects)
        self.assertTrue(student.created_at)

    def test_to_dict_and_from_dict(self):
        student = Student("S002", "Riya", 21, "Female", ["Java"])
        student_dict = student.to_dict()
        new_student = Student.from_dict(student_dict)
        self.assertEqual(new_student.name, "Riya")
        self.assertEqual(new_student.subjects, ["Java"])

class TestStudentManagementSystem(unittest.TestCase):

    def setUp(self):
        # Use a test file to avoid overwriting real data
        self.sms = StudentManagementSystem(data_file="test_students.json")
        self.sms.students = {}  # Clear any existing data

    def tearDown(self):
        import os
        if os.path.exists("test_students.json"):
            os.remove("test_students.json")

    def test_add_and_get_student(self):
        self.sms.add_student("S003", "Aman", 22, "Male", ["C++"])
        student = self.sms.get_student("S003")
        self.assertIsNotNone(student)
        self.assertEqual(student.name, "Aman")

    def test_update_student(self):
        self.sms.add_student("S004", "Neha", 19, "Female", ["Python"])
        self.sms.update_student("S004", name="Neha Sharma", age=20)
        student = self.sms.get_student("S004")
        self.assertEqual(student.name, "Neha Sharma")
        self.assertEqual(student.age, 20)

    def test_delete_student(self):
        self.sms.add_student("S005", "Rohan", 23, "Male", ["PHP"])
        self.sms.delete_student("S005")
        self.assertIsNone(self.sms.get_student("S005"))

    def test_search_students(self):
        self.sms.add_student("S006", "Priya", 20, "Female", ["Java"])
        results = self.sms.search_students("priya")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Priya")

if __name__ == '__main__':
    unittest.main()