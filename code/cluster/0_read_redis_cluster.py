from rediscluster import RedisCluster
import os

class RedisClusterSetting():

    def get_redis_cluster_info():

        if os.environ.get('REDIS_CLUSTER_HOST') == None:
            os.environ['REDIS_CLUSTER_HOST'] = 'redis_1,redis_2,redis_3'
        if os.environ.get('REDIS_CLUSTER_PORT') == None:
            os.environ['REDIS_CLUSTER_PORT'] = '6379,6379,6379'
        if os.environ.get('REDIS_CLUSTER_PASSWORD') == None:
            os.environ['REDIS_CLUSTER_PASSWORD'] = 'password'

        env_dict = {}

        for key, value in os.environ.items():
            env_dict.setdefault(key, value)

        redis_cluster_host = env_dict['REDIS_CLUSTER_HOST'].split(',')
        redis_cluster_port = env_dict['REDIS_CLUSTER_PORT'].split(',')
        redis_cluster_password = env_dict['REDIS_CLUSTER_PASSWORD']

        return redis_cluster_host, redis_cluster_port, redis_cluster_password

if __name__ == '__main__':

    redis_cluster_host, redis_cluster_port, redis_cluster_password = RedisClusterSetting.get_redis_cluster_info()

    for i in range(len(redis_cluster_host)):
        redis_host = redis_cluster_host[i]
        redis_port = redis_cluster_port[i]

        try:
            redis_client = RedisCluster(
                startup_nodes = [dict(host = redis_host, port = redis_port)],
                password = redis_cluster_password,
                decode_responses = True, 
                skip_full_coverage_check = True)
        except:
            print('Do not connected', redis_host)

    redis_client.set(2, 3)
    redis_client.expire(2, 5)
    print(redis_client.get(2))
