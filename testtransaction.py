import unittest
from datetime import datetime
from account import Account
from transaction import Transaction
from person import Person

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.person = Person("craig", "c", "a", "222-222-2222", "aaa")
        self.account = Account(10234, 1024, self.person.id)
        self.transaction = Transaction("withdrawal", 10, self.account.accountNum)

    def test_generate_id(self):
        # Test that generate_id() returns an integer with 5 digits
        transaction_id = self.transaction.generate_id()
        self.assertIsInstance(transaction_id, int)
        self.assertGreaterEqual(transaction_id, 0)
        self.assertLessEqual(transaction_id, 99999)
        self.assertEqual(len(str(transaction_id)), 5)

        # Test that generate_id() returns a unique ID
        transaction_id_2 = self.transaction.generate_id()
        self.assertNotEqual(transaction_id, transaction_id_2)

    def test_create_in_db(self):
        # Test that create_in_db() adds a transaction to the database
        self.transaction.create_in_db()
        retrieved_transaction = Transaction.retrieve(self.transaction.transaction_id)
        self.assertEqual(retrieved_transaction.type, self.transaction.type)
        self.assertEqual(retrieved_transaction.amount, self.transaction.amount)
        self.assertEqual(retrieved_transaction.account, self.transaction.account)
        self.assertEqual(retrieved_transaction.transaction_id, self.transaction.transaction_id)
        self.assertEqual(str(retrieved_transaction.date), str(self.transaction.date))

    def test_retrieve(self):
        # Test that retrieve() returns a Transaction object given a valid ID
        self.transaction.create_in_db()
        retrieved_transaction = Transaction.retrieve(self.transaction.transaction_id)
        self.assertEqual(retrieved_transaction.type, self.transaction.type)
        self.assertEqual(retrieved_transaction.amount, self.transaction.amount)
        self.assertEqual(retrieved_transaction.account, self.transaction.account)
        self.assertEqual(retrieved_transaction.transaction_id, self.transaction.transaction_id)
        self.assertEqual(str(retrieved_transaction.date), str(self.transaction.date))

        # Test that retrieve() returns None given an invalid ID
        invalid_transaction = Transaction.retrieve(99999)
        self.assertIsNone(invalid_transaction)

    def test_update_db(self):
        # Test that update_db() updates an existing transaction in the database
        self.transaction.create_in_db()
        new_date = datetime.now()
        self.transaction.date = new_date
        self.transaction.update_db()
        retrieved_transaction = Transaction.retrieve(self.transaction.transaction_id)
        self.assertEqual(str(retrieved_transaction.date), str(new_date))

    def test_delete_from_db(self):
        # Test that delete_from_db() removes a transaction from the database
        self.transaction.create_in_db()
        self.transaction.delete_from_db()
        retrieved_transaction = Transaction.retrieve(self.transaction.transaction_id)
        self.assertIsNone(retrieved_transaction)

    def tearDown(self):
        self.transaction.delete_from_db()

if __name__ == '__main__':
    unittest.main()
