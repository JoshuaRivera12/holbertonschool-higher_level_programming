#!/usr/bin/python3

"""
This Functiion will be able to get infromations from API's using request annd CURL
"""


import requests
import csv


def fetch_and_print_posts():
    responce = requests.get("https://jsonplaceholder.typicode.com/posts")
    responce.status_code
    print("Status Code:", responce.status_code)


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        posts_list = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in data
        ]

        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts_list)


            for post in data:
                print(post["title"], flush=True)

