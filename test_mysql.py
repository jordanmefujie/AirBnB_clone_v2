#!/usr/bin/python3
import unittest
import mysql.connector

class TestCreateStateCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a connection to the MySQL database
        cls.db_connection = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='your_test_database'
        )
        cls.cursor = cls.db_connection.cursor()

    @classmethod
    def tearDownClass(cls):
        # Close the database connection after all tests are done
        cls.cursor.close()
        cls.db_connection.close()

    def test_create_state_command(self):
        # Get the initial number of records in the states table
        initial_count = self._get_record_count()

        # Execute the console command to create a new state (e.g., using subprocess or other method)

        # Get the updated number of records in the states table
        updated_count = self._get_record_count()

        # Assert that the difference is +1
        self.assertEqual(updated_count - initial_count, 1)

    def _get_record_count(self):
        # Helper method to get the number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        return self.cursor.fetchone()[0]

if __name__ == '__main__':
    unittest.main()

