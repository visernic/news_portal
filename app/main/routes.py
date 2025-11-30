from flask import render_template, request, current_app
from app.main import main
from app.models import Post, Category

@main.route('/')
@main.route('/index')
def index():
    """
    Render the homepage with paginated news posts.
    """
    page = request.args.get('page', 1, type=int)
    
    # Fetch posts ordered by newest first
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    
    posts = pagination.items
    
    # Fetch recent categories for sidebar/filter (Optional optimization)
    categories = Category.query.all()
    
    return render_template('home/index.html', 
                           title='Home', 
                           posts=posts, 
                           categories=categories,
                           pagination=pagination)

@main.route('/about')
def about():
    """Render the static About Us page."""
    return render_template('main/about.html', title='About Us')
