#!/usr/bin/env python3
import argparse
import sys
import requests
import csv
from urllib.parse import urljoin


def send_post_request(url, data):
    response = requests.post(url, data)
    assert response.status_code == 202


def generate_users(base_url):
    url = urljoin(base_url, 'users/')

    with open('thesis_users.csv', 'r') as infile:
        reader = csv.reader(infile)
        for email, name in reader:
            data = {
                "email": email,
                "name": name
            }
            send_post_request(url, data)


def generate_restaurants(base_url):
    url = urljoin(base_url, 'restaurants/')

    with open('thesis_restaurants.csv', 'r') as infile:
        reader = csv.reader(infile)
        for title, address in reader:
            data = {
                "title": title,
                "address": address
            }
            send_post_request(url, data)


def generate_reviews(base_url):
    url = urljoin(base_url, 'reviews/')

    with open('thesis_reviews.csv', 'r') as infile:
        reader = csv.reader(infile)
        for title, content, user_id, restaurant_id in reader:
            data = {
                "title": title,
                "content": content,
                "user_id": user_id,
                "restaurant_id": restaurant_id
            }
            send_post_request(url, data)


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument('-u', '--url', required=True, help='Base url.')
    args = p.parse_args(argv)

    generate_users(args.url)
    generate_restaurants(args.url)
    generate_reviews(args.url)
    print("Data successfully generated.")


if __name__ == "__main__":
    argv = sys.argv[1:]
    sys.exit(main(argv))
