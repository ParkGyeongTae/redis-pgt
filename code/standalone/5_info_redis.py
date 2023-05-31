import os
import redis
import pprint

class RedisSetting():

    def get_redis_info():

        if os.environ.get('REDIS_HOST') == None:
            os.environ['REDIS_HOST'] = 'redis'
        if os.environ.get('REDIS_PORT') == None:
            os.environ['REDIS_PORT'] = '6379'
        if os.environ.get('REDIS_PASSWORD') == None:
            os.environ['REDIS_PASSWORD'] = 'password'

        env_dict = {}

        for key, value in os.environ.items():
            env_dict.setdefault(key, value)

        redis_host = env_dict['REDIS_HOST']
        redis_port = env_dict['REDIS_PORT']
        redis_password = env_dict['REDIS_PASSWORD']

        return redis_host, redis_port, redis_password

if __name__ == '__main__':

    redis_host, redis_port, redis_password = RedisSetting.get_redis_info()

    redis_client = redis.StrictRedis(host = redis_host, port = redis_port, db = 0, password = redis_password)

    redis_info = redis_client.info()
    print(f"role : {redis_info['role']}")
    print(f"redis_version : {redis_info['redis_version']}")
    print(f"redis_mode : {redis_info['redis_mode']}")
    print(f"connected_slaves : {redis_info['connected_slaves']}")
    print(f"connected_clients : {redis_info['connected_clients']}")
    print(f"total_system_memory_human : {redis_info['total_system_memory_human']}")
    print(f"used_memory_human : {redis_info['used_memory_human']}")
    print(f"used_memory_rss_human : {redis_info['used_memory_rss_human']}")
