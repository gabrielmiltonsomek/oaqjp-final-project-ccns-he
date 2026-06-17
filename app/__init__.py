"""
Flask Application with Security
"""
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

def create_app():
    """Create Flask app with security"""
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Add Talisman security headers
    Talisman(app, force_https=False)
    
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app

app = create_app()
