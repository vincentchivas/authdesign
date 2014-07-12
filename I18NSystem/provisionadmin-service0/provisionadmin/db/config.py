'''
Created on Jul 8, 2014

@author: xshu 
'''
import logging
from pymongo import Connection
from provisionadmin.db.mongodb_proxy import MongoProxy
from provisionadmin import settings


_LOGGER = logging.getLogger(__name__)


def _config_db(conn_str):
    assert conn_str

    try:
        _raw_conn = Connection(host=conn_str,
                               max_pool_size=20,
                               safe=True,
                               network_timeout=5)


        return _raw_conn
    except Exception, e:
        _LOGGER.critical(e)
        raise e


raw_conn_id = _config_db(settings.DB_SETTINGS['id'].get('host'))
raw_conn_user = _config_db(settings.DB_SETTINGS['user'].get('host'))
raw_conn_preset = _config_db(settings.DB_SETTINGS['preset'].get('host'))
raw_conn_trans = _config_db(settings.DB_SETTINGS['trans'].get('host'))

id_conn = MongoProxy(raw_conn_id, logger=_LOGGER, wait_time=10)
ID_DB = id_conn[settings.DB_SETTINGS['id'].get('name')] 

user_conn = MongoProxy(raw_conn_user, logger=_LOGGER, wait_time=10)
USER_DB = user_conn[settings.DB_SETTINGS['user'].get('name')] 

preset_conn = MongoProxy(raw_conn_preset, logger=_LOGGER, wait_time=10)
PRESET_DB = user_conn[settings.DB_SETTINGS['preset'].get('name')] 

trans_conn = MongoProxy(raw_conn_trans, logger=_LOGGER, wait_time=10)
TRANS_DB = user_conn[settings.DB_SETTINGS['trans'].get('name')] 
