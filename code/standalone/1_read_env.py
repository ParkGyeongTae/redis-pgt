import os
import pprint

# 1) 환경변수를 안이쁘게 출력 방법
# print(os.environ)

# 2) 환경변수를 이쁘게 출력하는 방법
# for key, value in os.environ.items():
#     print('{}: {}'.format(key, value))

# 3) 환경변수를 딕셔너리로 출력하는 방법
# env_dict = {}

# for key, value in os.environ.items():
#     env_dict.setdefault(key, value)

# pprint.pprint(env_dict)

# 4) 환경변수 관련 예외처리 하는 방법
env_dict = {}

if os.environ.get('redis_host') == None:
    os.environ['redis_host'] = 'redis'
if os.environ.get('redis_port') == None:
    os.environ['redis_port'] = '6379'

for key, value in os.environ.items():
    env_dict.setdefault(key, value)

pprint.pprint(env_dict)