"""
Account Routes Tests
"""
import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    """Test API routes"""
    
    def setUp(self):
        """Set up test client"""
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_health(self):
        """Test health endpoint"""
        response = self.client.get('/api/accounts/health')
        self.assertEqual(response.status_code, 200)
    
    def test_create_account(self):
        """Test create account"""
        data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone_number': '555-5678',
            'address': '456 Oak Ave'
        }
        response = self.client.post('/api/accounts', json=data)
        self.assertEqual(response.status_code, 201)
    
    def test_list_accounts(self):
        """Test list accounts"""
        response = self.client.get('/api/accounts')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
