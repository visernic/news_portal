from datetime import datetime
from app import db

class User(db.Model):
    """User model for storing admin or author details."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    # Relationship: One user can author many posts
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Category(db.Model):
    """Category model for organizing news posts."""
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    slug = db.Column(db.String(50), unique=True, nullable=False)
    
    # Relationship: One category can have many posts
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __repr__(self):
        return f'<Category {self.name}>'

class Post(db.Model):
    """News Post model."""
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    slug = db.Column(db.String(140), unique=True, index=True, nullable=False)
    summary = db.Column(db.String(300))
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), default='default.jpg')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return f'<Post {self.title}>'
