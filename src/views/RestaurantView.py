from flask import request, json, Response, Blueprint, g
from ..models.RestaurantModel import RestaurantModel, RestaurantSchema

restaurant_api = Blueprint('restaurants', __name__)
restaurant_schema = RestaurantSchema()


@restaurant_api.route('/', methods=['POST'])
def create():
    """
    Create Restaurant
    """
    req_data = request.get_json()
    data, error = restaurant_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    restaurant = RestaurantModel(data)
    restaurant.create()

    ser_data = restaurant_schema.dump(restaurant).data

    return custom_response(ser_data, 201)


@restaurant_api.route('/', methods=['GET'])
def get_all():
    """
    Get all restaurants.
    :return: List of all restaurants
    """
    restaurants = RestaurantModel.get_all_restaurants()
    ser_restaurants = restaurant_schema.dump(restaurants, many=True).data
    return custom_response(ser_restaurants, 200)


@restaurant_api.route('/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    """
    Get a single restaurant by id
    """
    restaurant = RestaurantModel.get_one_restaurant(restaurant_id)
    if not restaurant:
        return custom_response({'error': 'Restaurant not found.'}, 404)

    ser_restaurant = restaurant_schema.dump(restaurant).data
    return custom_response(ser_restaurant, 200)


@restaurant_api.route('/<int:restaurant_id>', methods=['PUT'])
def update(restaurant_id):
    """
    Update a restaurant
    """
    req_data = request.get_json()
    data, error = restaurant_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)

    restaurant = RestaurantModel.get_one_restaurant(restaurant_id)
    restaurant.update(data)
    ser_restaurant = restaurant_schema.dump(restaurant).data
    return custom_response(ser_restaurant, 200)


@restaurant_api.route('/<int:restaurant_id>', methods=['DELETE'])
def delete(restaurant_id):
    """
    Delete a restaurant
    """
    restaurant = RestaurantModel.get_one_restaurant(restaurant_id)
    if not restaurant:
        return custom_response({'error': 'Restaurant not found.'}, 404)
    restaurant.delete()
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
