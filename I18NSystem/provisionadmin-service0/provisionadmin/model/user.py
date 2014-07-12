from provisionadmin.utils.common import md5digest, unix_time
from provisionadmin.model.base import ModelBase


class User(ModelBase):
    
    @classmethod
    def new(cls, user_name, password='', group_id=0, permission_list=[]):
        '''
        create user
        '''
        instance = cls()
        instance.user_name = user_name
        if password:
            instance.password_hash = User.calc_password_hash(password)
        instance.group_id = group_id
        instance.permission_list = []
        instance.created = instance.modified = unix_time()
        instance.active = 1
        return instance

    def calc_password_hash(cls, password):
        return unicode(md5digest(password))

    def change_password(self, new_password):
        self.password_hash = User.calc_password_hash(new_password)
        self.modified = unix_time()

    def change_group(self, new_group_id):
        self.group_id = new_group_id
        self.modified = unix_time()

    def change_permission(self, new_permission_list):
        self.permission_list = new_permission_list
        self.modified = unix_time()


class Group(ModelBase):
    pass


class Permission(ModelBase):
    pass


class Session(ModelBase):
    pass



