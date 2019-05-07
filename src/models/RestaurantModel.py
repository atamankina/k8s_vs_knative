from marshmallow import fields, Schema
import datetime
from . import db
from .ReviewModel import ReviewSchema


class RestaurantModel(db.Model):
    """
    Restaurant Model
    """

    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    reviews = db.relationship('ReviewModel', backref='restaurants', lazy=True)

    def __init__(self, data):
        self.title = data.get('title')
        self.address = data.get('address')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def create(self):
        """
        Create Restaurant
        """
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """
        Update Restaurant
        :param data: Restaurant data to be updated
        """
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        """
        Delete Restaurant
        """
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_restaurants():
        """
        List all Restaurants
        :return: all Restaurants
        """
        return RestaurantModel.query.all()

    @staticmethod
    def get_one_restaurant(id):
        """
        Show Restaurant by id
        :param id: Restaurant id
        :return: Restaurant selected by id
        """
        return RestaurantModel.query.get(id)

    @staticmethod
    def get_restaurant_by_title(title):
        """
        Show Restaurant by title
        :param title: Restaurant title
        :return: Restaurant matched by title
        """
        return RestaurantModel.query.filter_by(title=title)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class RestaurantSchema(Schema):
    """
    Restaurant Schema
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    address = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    reviews = fields.Nested(ReviewSchema, many=True)
