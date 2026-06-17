"""
Account Model Tests
"""
import unittest
from app.models.account import Account

class TestAccount(unittest.TestCase):
    """Test Account model"""
    
    def setUp(self):
        """Set up test"""
        self.account = Account('John Doe', 'john@example.com', '555-1234', '123 Main St')
    
    def test_create_account(self):
        """Test creating an account"""
        self.assertEqual(self.account.name, 'John Doe')
        self.assertEqual(self.account.email, 'john@example.com')
    
    def test_to_dict(self):
        """Test account to_dict"""
        account_dict = self.account.to_dict()
        self.assertIn('name', account_dict)
        self.assertIn('email', account_dict)

if __name__ == '__main__':
    unittest.main()
