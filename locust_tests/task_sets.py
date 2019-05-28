from locust import HttpLocust, TaskSet
import os
from urllib.parse import urljoin

# ?? should I use random objects or always one object?
DATA = {
    "title": 'vestibulum velit id pretium iaculis',
    "content": 'Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.',
    "user_id": 52,
    "restaurant_id": 33
    }
OBJECT_ID = 10
BASE_URL = os.environ.get('BASE_URL', default='http://127.0.0.1:5000/')
REVIEWS_ENDPOINT = 'reviews/'
ONE_REVIEW_ENDPOINT = urljoin(REVIEWS_ENDPOINT, OBJECT_ID)
REVIEWS_BY_USER_ENDPOINT = urljoin(REVIEWS_ENDPOINT, 'user', OBJECT_ID)
REVIEWS_BY_RESTAURANT_ENDPOINT = urljoin(REVIEWS_ENDPOINT, 'restaurant', OBJECT_ID)


def get_one_review(l):
    l.client.get(ONE_REVIEW_ENDPOINT)


def get_all_reviews(l):
    l.client.get(REVIEWS_ENDPOINT)


def get_reviews_by_user(l):
    l.client.get(REVIEWS_BY_USER_ENDPOINT)


def get_reviews_by_restaurant(l):
    l.client.get(REVIEWS_BY_RESTAURANT_ENDPOINT)


def post_review(l):
    l.client.post(REVIEWS_ENDPOINT, json=DATA)


# expected quick response
class ReadOnlyOneObject(TaskSet):
    tasks = [get_one_review]


# expected slow response
class ReadOnlyAllObjects(TaskSet):
    tasks = [get_all_reviews]


# random response time - influencing factor - the length of reponse object...
# possible solution: use predefined set of objects to exclude the randomness
# of execution in different runs / in different environments
class ReadOnlyMultipleEndpoints(TaskSet):
    tasks = [get_one_review, get_all_reviews, get_reviews_by_user, get_reviews_by_restaurant]


class WriteOnly(TaskSet):
    tasks = [post_review]


# the same concerns as for multiple endpoints
class ReadWrite(TaskSet):
    tasks = {get_one_review: 5, get_all_reviews: 1,
             get_reviews_by_user: 1, get_reviews_by_restaurant: 3,
             post_review: 4}
