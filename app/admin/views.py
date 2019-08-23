from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import PostRespondForm
from .. import db
from ..models import Post, Student


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

"""""
----------------------------------------------------------------------
    Post Views
----------------------------------------------------------------------
"""""
#list all posts
@admin.route('/inquiries')
@login_required
def list_posts():
    """
    List all posts
    """
    #check_admin()
    
    posts = Post.query.all()
    
    return render_template('admin/posts/posts.htm',
                           posts=posts, title='Posts')

#assign department and salary
@admin.route('/respond/<int:id>', methods=['GET', 'POST'])
@login_required
def respond_post(id):
    """
    Assign a department and a salary to an employee
    """
    #check_admin()
    post = Post.query.filter_by(id=id).first()
    

    # prevent admin from being assigned a department or role
    #if employee.is_admin:
     #   abort(403)

    form = PostRespondForm(obj=post)
    if form.validate_on_submit():
        post.response = form.response.data
        db.session.add(post)
        db.session.commit()

        flash('You have successfully responded to enquiry from '+ post.student.name + " (" + post.student.admission +
                ")")

        # redirect to the roles page
        return redirect(url_for('admin.list_posts'))

    return render_template('admin/posts/response.htm',
                           post=post, form=form,
                           title='Respond Post')

#assign department and salary
@admin.route('/print/<int:id>', methods=['GET', 'POST'])
@login_required
def print(id):
    """
    Assign a department and a salary to an employee
    """
    #check_admin()

    #response = Response.query.get_or_404(id)
    post = Post.query.filter_by(id=id).first()
    response=Response()

    # prevent admin from being assigned a department or role
    #if employee.is_admin:
     #   abort(403)

    form = PostRespondForm(obj=response)
    if form.validate_on_submit():
        response.response = form.response.data
        db.session.add(response)
        db.session.commit()
        flash('You have successfully assigned a department and salary')

        # redirect to the roles page
        return redirect(url_for('admin.list_posts'))

    return render_template('admin/posts/response.htm',
                           post=post, form=form,
                           title='Print')

#delete a post
@admin.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    """
    Delete a post from the database
    """
    #check_admin()

    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('You have successfully deleted the post.')

    # redirect to the roles page
    return redirect(url_for('admin.list_posts'))

    return render_template(title="Delete Post")

"""""
----------------------------------------------------------------------
    Students Views
----------------------------------------------------------------------
"""""
#list all students
@admin.route('/students')
@login_required
def list_students():
    """
    List all students
    """
    #check_admin()
    
    students = Student.query.all()
    
    return render_template('admin/students/students.htm',
                           students=students, title='Students')