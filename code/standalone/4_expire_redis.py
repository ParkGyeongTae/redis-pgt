import os
import redis
import time

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

    redis_client.set('key_1', 'value_1')
    redis_client.expire('key_1', 10)

    start_time = time.time()

    for count in range(1, 16):
        time.sleep(1)
        end_time = time.time()
        print(f'- {count} -')
        print('time : %.2f, value : %s, ttl : %s, exists : %s'%(round(end_time - start_time, 2), redis_client.get('key_1'), redis_client.ttl('key_1'), redis_client.exists('key_1')))
