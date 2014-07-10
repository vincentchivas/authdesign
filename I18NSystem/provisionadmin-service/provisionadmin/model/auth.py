from db import  dbop

class AuthUser:
    def __init__(self,_id=0,name=None,password=None,email=None,is_active=True,is_superuser=False ,groupid=None,permissionIds=None):
        self._id=_id
        self.name=name
        self.password=password
        self.email=email
        self.is_active=is_active
        self.is_superuser=is_superuser
        self.groupid=groupid
        self.permissionIds=permissionIds

    def save(self):
        #check instance fields
        dbop.save(self)
    
    def delete(self):
        dbop.delete(self)

