from marshmallow import fields, Schema
import datetime
from . import db
from .ReviewModel import ReviewSchema


class UserModel(db.Model):
    """
    User Model
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    reviews = db.relationship('ReviewModel', backref='users', lazy=True)

    def __init__(self, data):
        self.name = data.get('name')
        self.email = data.get('email')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def create(self):
        """
        Create User
        """
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """
        Update User
        :param data: user data to be updated
        """
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        """
        Delete User
        """
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        """
        List all users
        :return: all users
        """
        return UserModel.query.all()

    @staticmethod
    def get_one_user(id):
        """
        Show user by id
        :param id: user id
        :return: user selected by id
        """
        return UserModel.query.get(id)

    @staticmethod
    def get_user_by_email(email):
        """
        Show user by email
        :param email: user email
        :return: user matched by email
        """
        return UserModel.query.filter_by(email=email).first()

    def __repr__(self):
        return '<id {}>'.format(self.id)


class UserSchema(Schema):
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    reviews = fields.Nested(ReviewSchema, many=True)
