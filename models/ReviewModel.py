from . import db
import datetime
from marshmallow import fields, Schema


class ReviewModel(db.Model):
    """
    Restaurant Review Model
    """

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.title = data.get('title')
        self.content = data.get('content')
        self.user_id = data.get('user_id')
        self.restaurant_id = data.get('restaurant_id')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def create(self):
        """
        Create review
        :return:
        """
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """
        Update review
        :param data:
        :return:
        """
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        """
        Delete review
        :return:
        """
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_reviews():
        """
        Get all reviews
        :return: all reviews
        """
        return ReviewModel.query.all()

    @staticmethod
    def get_one_review(id):
        """
        Get specific review by id
        :param id: review id
        :return: review matched by id
        """
        return ReviewModel.query.get(id)

    @staticmethod
    def get_reviews_by_user(user_id):
        """
        Get reviews by user id
        :param user_id: user id
        :return: reviews by user id
        """
        return ReviewModel.query.filter_by(user_id=user_id)

    @staticmethod
    def get_reviews_by_restaurant(restaurant_id):
        """
        Get reviews by restaurant id
        :param restaurant_id: restaurant id
        :return: reviews by restaurant id
        """
        return ReviewModel.query.filter_by(restaurant_id=restaurant_id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class ReviewSchema(Schema):
    """
    Restaurant Review Schema
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    user_id = fields.Int(required=True)
    restaurant_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
