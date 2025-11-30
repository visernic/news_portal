from flask import Blueprint

# Define the blueprint for news-related functionality
news = Blueprint('news', __name__)

# Import routes to register them with the blueprint
from . import routes
