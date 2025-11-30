from datetime import datetime

def format_date(date_obj):
    """
    Formats a datetime object into a user-friendly string.
    Example: '01 Dec, 2025'
    """
    if date_obj is None:
        return ""
    return date_obj.strftime('%d %b, %Y')

def generate_slug(text):
    """
    Generates a URL-friendly slug from a string.
    Example: 'New AI Tool' -> 'new-ai-tool'
    """
    return text.lower().replace(' ', '-')
