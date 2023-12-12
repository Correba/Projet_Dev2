"""import necessary to use and test the classes"""
import datetime
import unittest

from libs.classes.empty_value import EmptyValue
from libs.classes.evidence import Evidence
from libs.classes.investigation import Investigation
from libs.classes.person import Person


class InvestigationTestCase(unittest.TestCase):
    """
    Class use to test the Investigation class
    """

    def test_definition(self):
        """
        Test the definition of an Investigation
        """
        investigation1 = Investigation("test1")
        self.assertEqual(investigation1.name, "test1")
        self.assertEqual(investigation1.evidence, [])
        self.assertEqual(investigation1.people, [])
        self.assertEqual(investigation1.status, "In progress")

        investigation2 = Investigation("test2", "Over")
        self.assertEqual(investigation2.name, "test2")
        self.assertEqual(investigation2.evidence, [])
        self.assertEqual(investigation2.people, [])
        self.assertEqual(investigation2.status, "Over")

    def test_add_evidence(self):
        """
        Test adding an evidence to the Investigation
        """
        investigation1 = Investigation("test1")
        investigation1.add_evidence("evidence1")
        self.assertEqual(investigation1.evidence, ["evidence1"])

        investigation2 = Investigation("test2")
        investigation2.add_evidence(1)
        self.assertEqual(investigation2.evidence, [1])

    def test_add_person(self):
        """
        Test adding a person to the Investigation
        """
        investigation1 = Investigation("test1")
        investigation1.add_people("person1")
        self.assertEqual(investigation1.people, ["person1"])

        investigation2 = Investigation("test2")
        investigation2.add_people(1)
        self.assertEqual(investigation2.people, [1])

    def test_set_status(self):
        """
        Test to set the status of the Investigation
        """
        investigation1 = Investigation("test1")
        investigation1.status = "Over"
        self.assertEqual(investigation1.status, "Over")

        investigation2 = Investigation("test2", "Over")
        investigation2.status = "In progress"
        self.assertEqual(investigation2.status, "In progress")

    def test_str(self):
        """
        Test the textual representation of the Investigation
        """
        self.assertEqual(str(Investigation("test1")), "Name: test1, proof: [], person: [], status: In progress")
        self.assertEqual(str(Investigation("test2", "Over")), "Name: test2, proof: [], person: [], status: Over")


class EvidenceTestCase(unittest.TestCase):
    """
    Class use to test the Evidence class
    """

    def test_empty_value(self):
        """
        Test if the EmptyValue error is raised
        """
        with self.assertRaises(EmptyValue):
            Evidence("test1")

        with self.assertRaises(EmptyValue):
            Evidence("test2", "description2", datetime.date(2023, 12, 1), "")

        with self.assertRaises(EmptyValue):
            Evidence("", "description3", datetime.date(2023, 12, 1), "file3")

        with self.assertRaises(EmptyValue):
            Evidence("")

    def test_value_error(self):
        """
        Test if the ValueError is raised
        """
        with self.assertRaises(ValueError):
            Evidence("test1", "description1", datetime.date(2023, 12, 31), "file1")

        with self.assertRaises(ValueError):
            Evidence("test2", "description2", datetime.date(2024, 1, 1), "file2")

        with self.assertRaises(ValueError):
            Evidence("test3", "description3", datetime.date(2999, 4, 16), "file3")

    def test_definition(self):
        """
        Test the definition of an Evidence
        """
        evidence1 = Evidence("test1", file="file1")
        self.assertEqual(evidence1.name, "test1")
        self.assertEqual(evidence1.description, "")
        self.assertEqual(str(evidence1.date), "2023-12-12")
        self.assertEqual(evidence1.file, "file1")

        evidence2 = Evidence("test2", "description2", datetime.date(2023, 1, 1), "file2")
        self.assertEqual(evidence2.name, "test2")
        self.assertEqual(evidence2.description, "description2")
        self.assertEqual(str(evidence2.date), "2023-01-01")
        self.assertEqual(evidence2.file, "file2")


class PersonTestCase(unittest.TestCase):
    """
    Class use to test the Person class
    """

    def test_value_error(self):
        """
        Test if the ValueError is raised
        """
        with self.assertRaises(ValueError):
            Person("lastname1", "firstname1", datetime.date(2023, 12, 31), "gender1")

        with self.assertRaises(ValueError):
            Person("lastname1", "firstname1", datetime.date(2024, 1, 1), "gender1")

        with self.assertRaises(ValueError):
            Person("lastname1", "firstname1", datetime.date(2999, 4, 16), "gender1")

    def test_definition(self):
        """
        Test the definition of a Person
        """
        person1 = Person("lastname1", "firstname1")
        self.assertEqual(person1.lastname, "lastname1")
        self.assertEqual(person1.firstname, "firstname1")
        self.assertEqual(str(person1.birthdate), "2023-12-12")
        self.assertEqual(person1.gender, "")

        person2 = Person("lastname2", "firstname2", datetime.date(2000, 4, 16), "Male")
        self.assertEqual(person2.lastname, "lastname2")
        self.assertEqual(person2.firstname, "firstname2")
        self.assertEqual(str(person2.birthdate), "2000-04-16")
        self.assertEqual(person2.gender, "Male")


if __name__ == "__main__":
    unittest.main()
