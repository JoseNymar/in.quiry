from flask import abort, render_template
from flask_login import current_user, login_required

from . import home
from ..models import Student, Post

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    enquiries = Post.query.filter_by(author=current_user.id)
    #enquiries_no=len(enquiries)

    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/posts')
@login_required
def list_posts():
    """
    Render the dashboard template on the /dashboard route
    """
    posts = Post.query.filter_by(author=current_user.id)

    return render_template('home/posts.htm', posts=posts, title="Posts")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    posts = Post.query.all()
    posts_no = len(posts)
    students = Student.query.all()
    students_no = len(students)
    return render_template('home/admin_dashboard.html', posts_no=posts_no, students_no=students_no,
                             title="Admin Dashboard")
