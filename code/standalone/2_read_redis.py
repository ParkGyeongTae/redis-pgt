import os
import redis

if os.environ.get('redis_host') == None:
    os.environ['redis_host'] = 'redis'
if os.environ.get('redis_port') == None:
    os.environ['redis_port'] = '6379'

env_dict = {}

for key, value in os.environ.items():
    env_dict.setdefault(key, value)

redis_host = env_dict['redis_host']
redis_port = env_dict['redis_port']

redis_client = redis.StrictRedis(host = redis_host, port = redis_port)

redis_client.set('1', '2')
redis_client.set('3', '4')

# print(redis_client.get('1'))
# print(redis_client.get('3'))

result_1 = redis_client.get('1')
print(f'result_1: {result_1}')
print(f'type(result_1): {type(result_1)}')

result_1_str = result_1.decode('utf-8')
print(f'result_1_str: {result_1_str}')
print(f'type(result_1_str): {type(result_1_str)}')

result_2 = redis_client.get('3')
print(f'result_2: {result_2}')
print(f'type(result_2): {type(result_2)}')

result_2_str = result_2.decode('utf-8')
print(f'result_2_str: {result_2_str}')
print(f'type(result_2_str): {type(result_2_str)}')