from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from ChatbotWebsite.config import Config
from dotenv import load_dotenv
import os

# Initialize the extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)
    app.static_folder = 'static'

    # Initialize the extensions
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    # Explicitly set MAIL_DEFAULT_SENDER after mail is initialized
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
    print(f"MAIL_DEFAULT_SENDER in __init__: {app.config.get('MAIL_DEFAULT_SENDER')}") # Debug print

    # Import the routes AFTER the app object is created
    from ChatbotWebsite.main.routes import main
    from ChatbotWebsite.chatbot.routes import chatbot
    from ChatbotWebsite.users.routes import users
    from ChatbotWebsite.errors.handlers import errors
    from ChatbotWebsite.journal.routes import journals

    # Register the routes
    app.register_blueprint(users)
    app.register_blueprint(chatbot)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(journals)

    return app
