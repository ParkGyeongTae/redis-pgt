import os
import redis

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

redis_host, redis_port, redis_password = get_redis_info()

redis_client = redis.StrictRedis(host = redis_host, port = redis_port, db = 0, password = redis_password)

redis_client.set('key_1', 'value_1')
redis_client.set('key_2', 'value_2')
redis_client.set('key_3', 'value_3')
redis_client.set('key_4', 'value_4')
redis_client.set('key_5', 'value_5')

print(redis_client.get('key_1'))
print(redis_client.get('key_2'))
print(redis_client.get('key_3'))
print(redis_client.get('key_4'))
print(redis_client.get('key_5'))

# redis_client.flushall()