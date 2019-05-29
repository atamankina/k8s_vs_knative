import csv
import random


def prepare_data():
    with open('../mock_data/thesis_reviews.csv', 'r') as infile:
        rows = list(csv.reader(infile))
        title, content, user_id, restaurant_id = rows[random.randint(1, 1000)]
        data = {
            "title": title,
            "content": content,
            "user_id": user_id,
            "restaurant_id": restaurant_id
        }
    return data
