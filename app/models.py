from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Student(UserMixin, db.Model):

    """
    create a student table
    """

    __tablename__='students'

    id = db.Column(db.Integer, primary_key=True)
    admission = db.Column(db.String(128))
    name = db.Column(db.String(128))
    home_number=db.Column(db.String(128))
    cell_number = db.Column(db.String(128))
    email = db.Column(db.String(128))
    post_id = db.relationship('Post', backref='student', lazy='dynamic')
    is_admin = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.id)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))

class Post(db.Model):

    """
    create a post table
    """

    __tablename__='posts'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('students.id'))
    cell_number = db.Column(db.String(128))
    email = db.Column(db.String(128))
    enquiry = db.Column(db.String(128))
    response = db.Column(db.String(128))

    