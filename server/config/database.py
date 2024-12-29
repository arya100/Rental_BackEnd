import os
from pymongo import MongoClient
from typing import List, Optional
from urllib.parse import quote_plus

username = quote_plus('gocargo')
password = quote_plus('Bluesky@2023')
cluster = "cluster0.gatf1.mongodb.net"
database_name = "mydatabase"

uri=f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)

#DB
db=client[database_name]

users_collection = db["users"]
cars_collection = db["cars"]