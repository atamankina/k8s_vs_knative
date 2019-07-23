from locust import HttpLocust, TaskSet
import os
from urllib.parse import urljoin
from functools import reduce

# ?? should I use random objects or always one object?
DATA = {
    "title": 'vestibulum velit id pretium iaculis',
    "content": 'Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.',
    "user_id": 52,
    "restaurant_id": 33
    }
OBJECT_ID = '10'
BASE_URL = os.environ.get('BASE_URL', default='http://127.0.0.1:5000/')
REVIEWS_ENDPOINT = 'reviews/'
ONE_REVIEW_ENDPOINT = urljoin(REVIEWS_ENDPOINT, OBJECT_ID)
REVIEWS_BY_USER_ENDPOINT = reduce(urljoin, [REVIEWS_ENDPOINT, 'user/', OBJECT_ID])
REVIEWS_BY_RESTAURANT_ENDPOINT = reduce(urljoin, [REVIEWS_ENDPOINT, 'restaurant/', OBJECT_ID])
HEADERS = {"Host": "reviews-app-webserver.default.example.com"}


def get_one_review(l):
    l.client.get(url=ONE_REVIEW_ENDPOINT, headers=HEADERS)


def get_all_reviews(l):
    l.client.get(url=REVIEWS_ENDPOINT, headers=HEADERS)


def get_reviews_by_user(l):
    l.client.get(url=REVIEWS_BY_USER_ENDPOINT, headers=HEADERS)


def get_reviews_by_restaurant(l):
    l.client.get(url=REVIEWS_BY_RESTAURANT_ENDPOINT, headers=HEADERS)


def post_review(l):
    l.client.post(url=REVIEWS_ENDPOINT, json=DATA, headers=HEADERS)


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


class FastUser(HttpLocust):
    host = BASE_URL
    min_wait = 1000
    max_wait = 1000


class SingleRead(FastUser):
    task_set = ReadOnlyOneObject


class ReadAll(FastUser):
    task_set = ReadOnlyAllObjects


class ReadMultiple(FastUser):
    task_set = ReadOnlyMultipleEndpoints


class SingleWrite(FastUser):
    task_set = WriteOnly


class MultipleReadWrite(FastUser):
    task_set = ReadWrite


class SlowUser(HttpLocust):
    host = BASE_URL
    min_wait = 60000 * 10
    max_wait = 60000 * 10


class SingleReadSlow(SlowUser):
    task_set = ReadOnlyOneObject
