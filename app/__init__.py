from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

# Initialize extensions globally, but without binding to a specific app yet
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    """
    Application Factory: Creates and configures an instance of the Flask application.
    
    Args:
        config_name (str): The configuration name ('development', 'production', etc.)
        
    Returns:
        app: The configured Flask application instance.
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions with the app context
    db.init_app(app)
    migrate.init_app(app, db)
    
    # -----------------------------------------------------------
    # Register Blueprints
    # Note: These modules will be created in the next step.
    # We import them inside the function to avoid circular dependencies.
    # -----------------------------------------------------------
    
    # Main Blueprint (Home, About, etc.)
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # News Blueprint (News listing, details)
    from app.news import news as news_blueprint
    app.register_blueprint(news_blueprint, url_prefix='/news')

    # Errors Blueprint (404, 500 handlers)
    from app.errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    return app
