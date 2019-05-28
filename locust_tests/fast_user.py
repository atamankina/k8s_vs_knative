from locust_tests.task_sets import *


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
