"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq4fndvk4rjsv9kll0-a.oregon-postgres.render.com",
        database="todo_tx4v",
        user="root",
        password="lzH8rkfIxzu8BjiO93n7khSubqAncRHO")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
