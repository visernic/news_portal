from flask import render_template
from app import db
from app.errors import errors

@errors.app_errorhandler(404)
def error_404(error):
    """
    Custom handler for 404 Not Found errors.
    """
    return render_template('errors/404.html', title='Page Not Found'), 404

@errors.app_errorhandler(500)
def error_500(error):
    """
    Custom handler for 500 Internal Server Errors.
    We rollback the database session to ensure data integrity.
    """
    db.session.rollback()
    return render_template('errors/500.html', title='Server Error'), 500
