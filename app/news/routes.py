from flask import render_template, abort
from app.news import news
from app.models import Post, Category

@news.route('/post/<string:slug>')
def post_detail(slug):
    """
    Render a single news post detail page.
    
    Args:
        slug (str): The unique slug of the post.
    """
    # Fetch post by slug, return 404 if not found
    post = Post.query.filter_by(slug=slug).first_or_404()
    
    return render_template('news/detail.html', 
                           title=post.title, 
                           post=post)

@news.route('/category/<string:slug>')
def category(slug):
    """
    Render a list of posts belonging to a specific category.
    
    Args:
        slug (str): The unique slug of the category.
    """
    # Fetch category by slug
    category = Category.query.filter_by(slug=slug).first_or_404()
    
    # Get all posts for this category (ordered by newest)
    posts = category.posts.order_by(Post.timestamp.desc()).all()
    
    return render_template('news/category.html', 
                           title=category.name, 
                           category=category, 
                           posts=posts)
