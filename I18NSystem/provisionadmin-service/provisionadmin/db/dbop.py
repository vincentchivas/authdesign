import pymongo
hostip='localhost'
port=27017
conn=pymongo.Connection(hostip,port)
dbname='authdb'
db=conn[dbname]

def insert(model):      
    collectname=model.__class__.__name__
    dict_data=model.__dict__
    collection=db[collectname]
    collection.insert(dict_data)

