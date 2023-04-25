import json
import random

from tqdm import tqdm

from redis.cluster import RedisCluster, ClusterNode

iteration = 5
begin_port = 8001
end_port = 8007
connections = [ClusterNode("localhost", port) for port in range(begin_port, end_port)]
json_path = "./data/animes_raw.json"
cluster = RedisCluster(startup_nodes=connections, decode_responses=True)
type_data = [
    cluster.set,
    cluster.hset,
    cluster.zadd,
    cluster.lpush
]
name = "anime:rating"

avg_times = lambda x: sum(x) / len(x)
read_times = []
write_times = []

with open(json_path, 'r', encoding="utf8") as json_file:
    data = json.loads(json_file.read())


def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        delta = time.time() - start
        return delta

    return wrapper


@benchmark
def write():
    for anime in data:
        cluster.lpush(name, str(anime))


@benchmark
def read():
    index = random.randint(0, len(data))
    print(cluster.lindex(name, index))


for i in tqdm(range(iteration)):
    write_times.append(write())
    read_times.append(read())
    cluster.flushall()

print(f"AVG time writing: {avg_times(write_times)}")
print(f"AVG time reading: {avg_times(read_times)}")
