import os

from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient

# import pprint


# from etender_get_data import *
# print(my_data)

load_dotenv(find_dotenv())
# get password from env file
password = os.getenv("MONGODB_PW")

# connection_string = f"mongodb+srv://medo00001:{password}@cluster0.1k8ou.mongodb.net/?retryWrites=true&w=majority"

connection_string = (
    f"mongodb+srv://medo00001:{password}@cluster0.1k8ou.mongodb.net/test"
)
# connect to client
client = MongoClient(connection_string)
# get databases names
dbs = client.list_database_names()
# print(dbs)
# it will print ['test_db', 'admin', 'local']
# cinnect to db
my_db_connect = client.test_db
# or using my_db_connect = client['test_db']
# get all collections names
collections = my_db_connect.list_collection_names()
# print(collections)
# it will get all collections names from test_db database
# ['etender_collection']


# insert document to collection etender_collection
def insert_document(document):
    my_db_connect.etender_collection.insert_one(document)


def insert_many(document):
    my_db_connect.etender_collection.insert_many(document)


# -------------------- delete collection *-----------------
def drop_tender_collection():
    mydb = client["test_db"]
    mycollection = mydb["etender_collection"]
    mycollection.drop()


# ====================================================================
