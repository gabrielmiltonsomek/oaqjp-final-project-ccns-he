"""
Account Routes
"""
from flask import Blueprint, request, jsonify
from app.models.account import Account

bp = Blueprint('accounts', __name__, url_prefix='/api/accounts')

# In-memory storage (replace with database in production)
accounts = {}
next_id = 1

@bp.route('', methods=['POST'])
def create_account():
    """Create an account"""
    global next_id
    data = request.get_json()
    account = Account(
        name=data['name'],
        email=data['email'],
        phone_number=data.get('phone_number'),
        address=data.get('address')
    )
    account.id = next_id
    next_id += 1
    accounts[account.id] = account
    return jsonify(account.to_dict()), 201

@bp.route('', methods=['GET'])
def list_accounts():
    """List all accounts"""
    return jsonify([acc.to_dict() for acc in accounts.values()]), 200

@bp.route('/<int:account_id>', methods=['GET'])
def read_account(account_id):
    """Read an account"""
    if account_id not in accounts:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(accounts[account_id].to_dict()), 200

@bp.route('/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    """Update an account"""
    if account_id not in accounts:
        return jsonify({'error': 'Not found'}), 404
    data = request.get_json()
    account = accounts[account_id]
    account.name = data.get('name', account.name)
    account.email = data.get('email', account.email)
    account.phone_number = data.get('phone_number', account.phone_number)
    account.address = data.get('address', account.address)
    return jsonify(account.to_dict()), 200

@bp.route('/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    """Delete an account"""
    if account_id not in accounts:
        return jsonify({'error': 'Not found'}), 404
    del accounts[account_id]
    return '', 204

@bp.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({'status': 'UP'}), 200
