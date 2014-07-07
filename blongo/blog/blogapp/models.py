from mongoengine import *
from blog.settings import DBNAME,INSTALLED_APPS

connect(DBNAME)
DBMODELS=['Post','AuthGroup','AuthUser']
Operations=['add','change','delete']

class AllPermissions(Document):
    name=StringField(max_length=50)
    app_label=StringField(max_length=100)
    model=StringField(max_length=100)
    operator=StringField(max_length=100)  #add change delete ,like this  'add_permission'


class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
    tags = ListField(StringField(max_length=30))

class Permission(EmbeddedDocument):
    name=StringField(max_length=50)
    app_label=StringField(max_length=100)
    model=StringField(max_length=100)
    operator=StringField(max_length=100)  #add change delete ,like this  'add_permission'

class AuthGroup(Document):
    name=StringField(max_length=50)
    permissions=ListField(EmbeddedDocumentField(Permission))

class AuthUser(Document):
    username = StringField(max_length=50,required=True)
    password = StringField(max_length=50,required=True)
    email = EmailField()
    is_staff = BooleanField(default=1)
    is_active = BooleanField(default=1)
    is_superuser = BooleanField(default=1)
    groupname=StringField(max_length=50)
    permissions=ListField(EmbeddedDocumentField(Permission))

def initialpermissions():  #initial  all  permissions label 
    AllPermissions.drop_collection()
    for app_name in INSTALLED_APPS:
        for model_name in DBMODELS:
            for op in Operations:
                name='can '+op+' '+model_name
                permission=AllPermissions(name=name,app_label=app_name,model=model_name,operator=op)
                permission.save()


