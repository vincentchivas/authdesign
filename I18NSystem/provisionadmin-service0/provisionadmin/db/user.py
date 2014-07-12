from provisionadmin.db.config import USER_DB
from provisionadmin.model.user import User
from provisionadmin.db.seqid import get_next_id


def save_user(user):
    assert user
    if not user._id:
        # assign sequential id
        user._id = get_next_id('user')
    USER_DB.user.save(user)
    return user


