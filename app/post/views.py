from flask import abort, render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from .forms import PostForm
from . import post
from .. import db
from ..models import Post

@post.route('/post', methods=['GET', 'POST'])
@login_required
def send_enquiry():
    """
    Render the post template on the /post route
    """
    
    form = PostForm()
    if form.validate_on_submit():
        author = current_user.id
        cell_number=form.cell_number.data
        email=form.email.data
        enquiry=form.enquiry.data
        post = Post( author=author, cell_number=cell_number,
                            email=email, enquiry=enquiry)

        # add post to the database
        db.session.add(post)
        db.session.commit()
        flash('You have successfully Posted! Kindly wait for a response')

        # redirect to the success page
        return redirect(url_for('home.list_posts'))

    # load post template
    return render_template('send/send.htm', form=form, title='Enquiry')

#edit department
@post.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_enquiry(id):
    """
    Edit an enquiry
    """

    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.cell_number = form.cell_number.data
        post.email = form.email.data
        post.enquiry = form.enquiry.data
        db.session.commit()
        flash('You have successfully edited the enquiry.')

        # redirect to the departments page
        return redirect(url_for('home.list_posts'))

    form.cell_number.data = post.cell_number
    form.email.data = post.email
    form.enquiry.data = post.enquiry
    return render_template('home/post.htm', action="Edit", form=form, title="Edit Enquiry")
