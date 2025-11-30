import unittest
from flask import current_app
from app import create_app, db

class BasicTestCase(unittest.TestCase):
    """Basic test cases for the application."""

    def setUp(self):
        """Set up the test environment before each test."""
        # Use 'testing' config which uses in-memory database
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Clean up after each test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        """Check if the app instance is created successfully."""
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """Ensure the app is running in testing mode."""
        self.assertTrue(current_app.config['TESTING'])

if __name__ == '__main__':
    unittest.main()
