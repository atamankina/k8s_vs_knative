from flask import request, g, Blueprint, json, Response
from ..models.ReviewModel import ReviewModel, ReviewSchema
from ..models.UserModel import UserModel
from ..models.RestaurantModel import RestaurantModel

review_api = Blueprint('review_api', __name__)
review_schema = ReviewSchema()


@review_api.route('/', methods=['POST'])
def create():
    """
    Create review
    """
    req_data = request.get_json()
    data, error = review_schema.load(req_data)
    if error:
        return custom_response(error, 400)

    user = UserModel.get_one_user(data.get('user_id'))
    if not user:
        return custom_response({'error': 'Cannot create review. User not found.'}, 404)

    restaurant = RestaurantModel.get_one_restaurant(data.get('restaurant_id'))
    if not restaurant:
        return custom_response({'error': 'Cannot create review. Restaurant not found.'}, 404)

    review = ReviewModel(data)
    review.create()
    data = review_schema.dump(review).data
    return custom_response(data, 201)


@review_api.route('/', methods=['GET'])
def get_all():
    """
    Get all reviews
    """
    reviews = ReviewModel.get_all_reviews()
    data = review_schema.dump(reviews, many=True).data
    return custom_response(data, 200)


@review_api.route('/<int:review_id>', methods=['GET'])
def get_one(review_id):
    """
    Get a review by id
    """
    review = ReviewModel.get_one_review(review_id)
    if not review:
        return custom_response({'error': 'Review not found'}, 404)
    data = review_schema.dump(review).data
    return custom_response(data, 200)


@review_api.route('/user/<int:user_id>', methods=['GET'])
def get_reviews_by_user(user_id):
    """
    Get reviews by user id
    """
    user = UserModel.get_one_user(user_id)
    if not user:
        return custom_response({'error': 'User not found.'}, 404)
    reviews = ReviewModel.get_reviews_by_user(user_id)
    data = review_schema.dump(reviews, many=True).data
    return custom_response(data, 200)


@review_api.route('/restaurant/<int:restaurant_id>', methods=['GET'])
def get_reviews_by_restaurant(restaurant_id):
    """
    Get reviews by restaurant id
    """
    restaurant = RestaurantModel.get_one_restaurant(restaurant_id)
    if not restaurant:
        return custom_response({'error': 'Restaurant not found.'}, 404)
    reviews = ReviewModel.get_reviews_by_restaurant(restaurant_id)
    data = review_schema.dump(reviews, many=True).data
    return custom_response(data, 200)


@review_api.route('/<int:review_id>', methods=['PUT'])
def update(review_id):
    """
    Update a review
    """
    req_data = request.get_json()
    review = ReviewModel.get_one_review(review_id)
    if not review:
        return custom_response({'error': 'Review not found.'}, 404)

    data, error = review_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)
    review.update(data)

    data = review_schema.dump(review).data
    return custom_response(data, 200)


@review_api.route('/<int:review_id>', methods=['DELETE'])
def delete(review_id):
    """
    Delete a review
    """
    review = ReviewModel.get_one_review(review_id)
    if not review:
        return custom_response({'error': 'Review not found.'}, 404)

    review.delete()
    return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
