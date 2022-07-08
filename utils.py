from pymongo import MongoClient


def get_db_handle(host, port, username, password):
    client = MongoClient(host="localhost",
                         port=int(27017),
                         username="admin",
                         password="admin"
                         )
    return client
