#!/usr/bin/python
import pymongo
hostip='localhost'
port=27017
conn=pymongo.Connection(hostip,port)
dbname='authdb'
db=conn[dbname]
#db['counters'].insert({'_id':'userid','seq':0})  initial counters ,add 

def getid(idname):
    item=db.seqs.find_one({'_id':idname})
    if  item == None:
        db.seqs.insert({'_id':idname,'seq':0})  #if not ,initial one 
    else:
        db.seqs.find_and_modify({'_id':idname},update={'$inc':{'seq':1}},upsert=True) 
    item=db.seqs.find_one({'_id':idname})
    return item['seq']    

def delete(model):
    collectname=model.__class__.__name__
    dict_data=model.__dict__
    collection=db[collectname]
    collection.remove(model.id)

def insert(model):      
    collectname=model.__class__.__name__
    dict_data=model.__dict__
    collection=db[collectname]
    dict_data['_id']=getid(collectname+'ids')
    collection.insert(dict_data)

def update(model):
    collectname=model.__class__.__name__
    dict_data=model.__dict__
    collection=db[collectname]
    collection.update({'_id':model.id},{'$set':dict_data)

