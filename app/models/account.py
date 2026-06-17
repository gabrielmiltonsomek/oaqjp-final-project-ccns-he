"""
Account Model
"""
from datetime import datetime

class Account:
    """Account class"""
    
    def __init__(self, name, email, phone_number, address):
        """Initialize Account"""
        self.id = None
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.date_joined = datetime.utcnow()
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'address': self.address,
            'date_joined': self.date_joined.isoformat()
        }
    
    def __repr__(self):
        return f"<Account {self.name}>"
