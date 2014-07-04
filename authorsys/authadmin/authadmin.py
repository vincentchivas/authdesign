from mongoengine import *
connect('test')

class Auser(Document):
    username = StringField(max_length=50,required=True)
    password = StringField(max_length=50,required=True)
    email = EmailField()
    is_staff = BooleanField()
    is_active = BooleanField()
    is_superuser = BooleanField()

class Agroup(Document):
    name=StringField(required=True)

class Apermission(Document):
    name=StringField(max_length=50)
    codename=StringField(max_length=100)

class Acontent_type(Document):
    name=StringField(max_length=100)
    app_label=StringField(max_length=100)
    model = StringField(max_length=100)



