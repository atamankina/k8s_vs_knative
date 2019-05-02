from flask import request, g, Blueprint, json, Response
from ..models.ReviewModel import ReviewModel, ReviewSchema

review_api = Blueprint('review_api', __name__)
review_schema = ReviewSchema()


@review_api.route('/', methods=['POST'])
def create():
    """
    Create review
    """
    req_data = request.get_json()
    req_data['owner_id'] = g.user.get('id')
    data, error = review_schema.load(req_data)
    if error:
        return custom_response(error, 400)
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


@review_api.route('/<int:review_id>', methods=['PUT'])
def update(review_id):
    """
    Update a review
    """
    req_data = request.get_json()
    review = ReviewModel.get_one_review(review_id)
    if not review:
        return custom_response({'error': 'Review not found.'}, 404)
    data = review_schema.dump(review).data

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
    data = review_schema.dump(review).data

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
