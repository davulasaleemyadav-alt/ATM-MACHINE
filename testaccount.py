import unittest
import sqlite3
from models.accountModel import Account

class AccountTest(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE ACCOUNT (
                accountNum INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_create_and_retrieve(self):
        # Test creating an account and retrieving it from the database
        acc = Account("John Doe", "johndoe", "password123", "johndoe@example.com", "1234567890", "123 Main St")
        acc.create_in_db()
        retrieved_acc = Account.retrieve(acc.accountNum)
        self.assertEqual(acc.name, retrieved_acc.name)
        self.assertEqual(acc.username, retrieved_acc.username)
        self.assertEqual(acc.password, retrieved_acc.password)
        self.assertEqual(acc.email, retrieved_acc.email)
        self.assertEqual(acc.phone, retrieved_acc.phone)
        self.assertEqual(acc.address, retrieved_acc.address)

    def test_update(self):
        # Test updating an existing account in the database
        acc = Account("John Doe", "johndoe", "password123", "johndoe@example.com", "1234567890", "123 Main St")
        acc.create_in_db()
        acc.phone = "0987654321"
        acc.update_db()
        retrieved_acc = Account.retrieve(acc.accountNum)
        self.assertEqual(acc.phone, retrieved_acc.phone)

if __name__ == '__main__':
    unittest.main()
