import unittest
from student_management_system import StudentManagementSystem

class TestStudentManagementSystem(unittest.TestCase):

    def setUp(self):
        # Use a test file to avoid overwriting real data
        self.sms = StudentManagementSystem(data_file="test_students.json")
        self.sms.students = {}  # Clear any existing data

    def tearDown(self):
        import os
        if os.path.exists("test_students.json"):
            os.remove("test_students.json")

    def test_add_student_success(self):
        success, message = self.sms.add_student("BU001", "Kavya Rana", 20, "Male", ["Python", "DBMS"])
        self.assertTrue(success)
        self.assertEqual(message, "Student added successfully")
        self.assertIn("BU001", self.sms.students)

    def test_add_student_duplicate(self):
        self.sms.add_student("BU002", "Riya", 21, "Female", ["Java"])
        success, message = self.sms.add_student("BU002", "Riya", 21, "Female", ["Java"])
        self.assertFalse(success)
        self.assertEqual(message, "Student with this ID already exists")

    def test_update_student_success(self):
        self.sms.add_student("BU003", "Aman", 22, "Male", ["C++"])
        success, message = self.sms.update_student("BU003", name="Aman Kumar", age=23)
        self.assertTrue(success)
        self.assertEqual(message, "Student updated successfully")
        self.assertEqual(self.sms.students["BU003"].name, "Aman Kumar")
        self.assertEqual(self.sms.students["BU003"].age, 23)

    def test_update_student_not_found(self):
        success, message = self.sms.update_student("BU999", name="Ghost")
        self.assertFalse(success)
        self.assertEqual(message, "Student not found")

    def test_delete_student_success(self):
        self.sms.add_student("BU004", "Neha", 19, "Female", ["PHP"])
        success, message = self.sms.delete_student("BU004")
        self.assertTrue(success)
        self.assertEqual(message, "Student deleted successfully")
        self.assertNotIn("BU004", self.sms.students)

    def test_delete_student_not_found(self):
        success, message = self.sms.delete_student("BU888")
        self.assertFalse(success)
        self.assertEqual(message, "Student not found")

    def test_search_students_by_name(self):
        self.sms.add_student("BU005", "Priya", 20, "Female", ["Java"])
        results = self.sms.search_students("priya")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Priya")

    def test_search_students_by_grade(self):
        self.sms.add_student("BU006", "Rohan", 23, "Male", ["Python"])
        results = self.sms.search_students("male")
        self.assertTrue(any(s.student_id == "BU006" for s in results))

if __name__ == '__main__':
    unittest.main()