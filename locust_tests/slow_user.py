from locust_tests.task_sets import *


class SlowUser(HttpLocust):
    host = BASE_URL
    min_wait = 60000 * 30
    max_wait = 60000 * 30


class SingleRead(SlowUser):
    task_set = ReadOnlyOneObject
