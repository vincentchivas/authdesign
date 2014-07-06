from mongoengine import *
from blog.settings import DBNAME

connect(DBNAME)

class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
    tags = ListField(StringField(max_length=30))

class content_type(EmbeddedDocument):
    name=StringField(max_length=100)
    app_label=StringField(max_length=100)
    model=StringField(max_length=100)

class Permission(EmbeddedDocument):
    name=StringField(max_length=50)
    content_type=EmbeddedDocumentField(content_type)
    codename=StringField(max_length=100)

class AuthGroup(Document):
    name=StringField(max_length=50)
    permissions=EmbeddedDocumentField(Permission)

class AuthUser(Document):
    username = StringField(max_length=50,required=True)
    password = StringField(max_length=50,required=True)
    email = EmailField()
    is_staff = BooleanField(default=1)
    is_active = BooleanField(default=1)
    is_superuser = BooleanField(default=1)
    groupname=StringField(max_length=50)
    permissions=EmbeddedDocumentField(Permission)

