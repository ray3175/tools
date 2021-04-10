from functools import wraps
import redis
from xy.decorator.singleton import Singleton
from xy.exception import XYException
from ...config import AppConfig
from . import Cache


@Singleton
class CacheRedis(Cache):
    def __init__(self):
        if AppConfig()["cache"]["serialize"] == "json":
            import json
            self.__serialize = json
        else:
            import pickle
            self.__serialize = pickle
        self.__init_redis()

    def __init_redis(self):
        self.__redis_config = AppConfig()["cache"]["redis"]
        self.__redis_pool = redis.ConnectionPool(password=self.__redis_config["password"], host=self.__redis_config["host"], port=self.__redis_config["port"], db=self.__redis_config["db"])
        self.__redis = redis.Redis(connection_pool=self.__redis_pool)

    def cache(self, name, args_name, serial=True, *args, **kwargs):
        """
        :param name: redis key 的前缀名称，如：person
        :param args_name: 作为 key 的参数名称
        :param serial: 是否序列化
        """
        def cache_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                args_value = name + "::" + self._extract_args_value(func, args_name, *args, **kwargs)
                try:
                    _return = self.__redis.get(args_value)
                except redis.exceptions.ConnectionError:
                    _return = None
                except Exception as e:
                    raise XYException(f"Redis服务出现异常！\n\t{e}")
                if _return:
                    if serial:
                        _return = self.__serialize.loads(_return)
                else:
                    if _return:=func(*args, **kwargs):
                        try:
                            self.__redis.set(args_value, self.__serialize.dumps(_return) if serial else _return, ex=self.__redis_config["ex"])
                        except redis.exceptions.ConnectionError:
                            pass
                        except Exception as e:
                            raise XYException(f"Redis服务出现异常！\n\t{e}")
                return _return
            return action
        return cache_action

