from flask import request, json, Response, Blueprint, g
from ..models.UserModel import UserModel, UserSchema

user_api = Blueprint('users', __name__)
user_schema = UserSchema()


@user_api.route('/', methods=['POST'])
def create():
    """
    Create User
    """
    req_data = request.get_json()
    data, error = user_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    # check if user already exist in the db
    user_in_db = UserModel.get_user_by_email(data.get('email'))
    if user_in_db:
        message = {'error': 'User with this e-mail address already exists.'}
        return custom_response(message, 400)

    user = UserModel(data)
    user.create()

    ser_data = user_schema.dump(user).data

    return custom_response(ser_data, 201)


@user_api.route('/', methods=['GET'])
def get_all():
    """
    Get all users
    :return: list of all users
    """
    users = UserModel.get_all_users()
    ser_users = user_schema.dump(users, many=True).data
    return custom_response(ser_users, 200)


@user_api.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a single user by id
    """
    user = UserModel.get_one_user(user_id)
    if not user:
        return custom_response({'error': 'User not found.'}, 404)

    ser_user = user_schema.dump(user).data
    return custom_response(ser_user, 200)


@user_api.route('/<int:user_id>', methods=['PUT'])
def update(user_id):
    """
    Update a user
    """
    req_data = request.get_json()
    data, error = user_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)

    user = UserModel.get_one_user(user_id)
    user.update(data)
    ser_user = user_schema.dump(user).data
    return custom_response(ser_user, 200)


@user_api.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    """
    Delete a user
    """
    user = UserModel.get_one_user(user_id)
    if not user:
        return custom_response({'error': 'User not found.'}, 404)
    user.delete()
    return custom_response({'result': 'User deleted.'}, 204)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
