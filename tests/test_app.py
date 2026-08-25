import unittest
from app import search_students


class TestSearchStudents(unittest.TestCase):

    def test_find_student(self):
        result = search_students("Nguyen Van An")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Nguyen Van An")

    def test_student_not_found(self):
        result = search_students("Le Van Cuong")
        self.assertEqual(result, [])

    def test_search_case_insensitive(self):
        result = search_students("nguyen")
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
