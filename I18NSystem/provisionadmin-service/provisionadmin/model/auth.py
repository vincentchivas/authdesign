class AuthUser:
    def __init__(self,name,password,email=None,is_active=True,is_superuser=False ,groupid=None,permissionIds=None):
        self.name=name
        self.password=password
        self.email=email
        self.is_active=is_active
        self.is_superuser=is_superuser
        self.groupid=groupid
        self.permissionIds=permissionIds


