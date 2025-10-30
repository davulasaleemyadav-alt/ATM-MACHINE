import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Alan", "Le", "alanle@alanlecompany.com", "555-555-5555", "123 Main St.")

    def test_create_and_retrieve_person(self):
        # Create a new person
        self.person.create_in_db()

        # Retrieve the person from the database
        retrieved_person = Person.retrieve(self.person.id)

        # Ensure that the retrieved person matches the original person
        self.assertEqual(self.person.first_name, retrieved_person.first_name)
        self.assertEqual(self.person.last_name, retrieved_person.last_name)
        self.assertEqual(self.person.email_address, retrieved_person.email_address)
        self.assertEqual(self.person.telephone_number, retrieved_person.telephone_number)
        self.assertEqual(self.person.physical_address, retrieved_person.physical_address)

    def test_update_person(self):
        # Create a new person
        self.person.create_in_db()

        # Update the person's information
        self.person.first_name = "Update"
        self.person.update_db()

        # Retrieve the person from the database
        retrieved_person = Person.retrieve(self.person.id)

        # Ensure that the retrieved person's information has been updated
        self.assertEqual(self.person.first_name, retrieved_person.first_name)

    def test_delete_person(self):
        # Create a new person
        self.person.create_in_db()

        # Delete the person from the database
        self.person.delete_from_db()

        # Attempt to retrieve the person from the database
        retrieved_person = Person.retrieve(self.person.id)

        # Ensure that the retrieved person is None (i.e. does not exist)
        self.assertIsNone(retrieved_person)

        
    def tearDown(self):
        self.person.delete_from_db()

if __name__ == '__main__':
    unittest.main()
