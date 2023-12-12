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

        investigation3 = Investigation('test3')
        evidence = Evidence("evidence", "description", datetime.date(2023, 12, 1), "file")
        investigation3.add_evidence(evidence)
        self.assertTrue(evidence in investigation3.evidence)

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

        investigation3 = Investigation('test3')
        person = Person("lastname", "firstname")
        investigation3.add_people(person)
        self.assertTrue(person in investigation3.people)

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
        investigation3 = Investigation('test3')
        person = Person("lastname", "firstname")
        investigation3.add_people(person)
        self.assertEqual(str(investigation3), f'Name: test3, proof: [], person: [{person}], status: In progress')
        investigation4 = Investigation('test4')
        evidence = Evidence("evidence", "description", datetime.date(2023, 12, 1), "file")
        investigation4.add_evidence(evidence)
        self.assertEqual(str(investigation4), f'Name: test4, proof: [{evidence}], person: [], status: In progress')
        investigation5 = Investigation('test5')
        investigation5.add_evidence(evidence)
        investigation5.add_people(person)
        self.assertEqual(str(investigation5), f'Name: test5, proof: [{evidence}], person: [{person}], status: In progress')


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
        with self.assertRaises(ValueError) as error_1:
            Evidence("test1", "description1", datetime.date(2023, 12, 31), "file1")
        self.assertEqual(error_1.exception.args[0], 'Proof date cannot be in the future')

        with self.assertRaises(ValueError) as error_2:
            Evidence("test2", "description2", datetime.date(2024, 1, 1), "file2")
        self.assertEqual(error_2.exception.args[0], 'Proof date cannot be in the future')

        with self.assertRaises(ValueError) as error_3:
            Evidence("test3", "description3", datetime.date(2999, 4, 16), "file3")
        self.assertEqual(error_3.exception.args[0], 'Proof date cannot be in the future')

    def test_definition(self):
        """
        Test the definition of an Evidence
        """
        evidence1 = Evidence("test1", file="file1")
        self.assertEqual(evidence1.name, "test1")
        self.assertEqual(evidence1.description, "")
        self.assertEqual(evidence1.date, datetime.date.today())
        self.assertEqual(evidence1.file, "file1")

        year, month, day = [2023, 1, 1]
        evidence2 = Evidence("test2", "description2", datetime.date(year, month, day), "file2")
        self.assertEqual(evidence2.name, "test2")
        self.assertEqual(evidence2.description, "description2")
        self.assertEqual(evidence2.date, datetime.date(year, month, day))
        self.assertEqual(evidence2.file, "file2")


class PersonTestCase(unittest.TestCase):
    """
    Class use to test the Person class
    """

    def test_value_error(self):
        """
        Test if the ValueError is raised
        """
        with self.assertRaises(ValueError) as error_1:
            Person("lastname1", "firstname1", datetime.date(2023, 12, 31), "gender1")
        self.assertEqual(error_1.exception.args[0], 'Birthdate cannot be in the future')

        with self.assertRaises(ValueError) as error_2:
            Person("lastname1", "firstname1", datetime.date(2024, 1, 1), "gender1")
        self.assertEqual(error_2.exception.args[0], 'Birthdate cannot be in the future')

        with self.assertRaises(ValueError) as error_3:
            Person("lastname1", "firstname1", datetime.date(2999, 4, 16), "gender1")
        self.assertEqual(error_3.exception.args[0], 'Birthdate cannot be in the future')

    def test_empty_error(self):
        """
        Test if the EmptyValue error is raised
        """
        with self.assertRaises(EmptyValue) as error_1:
            Person("", "firstname1")
        self.assertEqual(error_1.exception.args[0], 'Lastname cannot be empty')

        with self.assertRaises(EmptyValue) as error_2:
            Person("lastname1", "")
        self.assertEqual(error_2.exception.args[0], 'Firstname cannot be empty')

        with self.assertRaises(EmptyValue) as error_3:
            Person("", "")
        self.assertEqual(error_3.exception.args[0], 'Lastname cannot be empty')

    def test_definition(self):
        """
        Test the definition of a Person
        """
        person1 = Person("lastname1", "firstname1")
        self.assertEqual(person1.lastname, "lastname1")
        self.assertEqual(person1.firstname, "firstname1")
        self.assertEqual(person1.birthdate, datetime.date.today())
        self.assertEqual(person1.gender, "")

        year, month, day = [2000, 4, 15]
        person2 = Person("lastname2", "firstname2", datetime.date(year, month, day), "Male")
        self.assertEqual(person2.lastname, "lastname2")
        self.assertEqual(person2.firstname, "firstname2")
        self.assertEqual(person2.birthdate, datetime.date(year, month, day))
        self.assertEqual(person2.gender, "Male")


if __name__ == "__main__":
    unittest.main()
