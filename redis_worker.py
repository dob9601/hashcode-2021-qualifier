import redis
from world2 import World
import pickle

host = "192.168.0.34"

if __name__ == "__main__":
    red = redis.Redis(host, port=6379, db=0)
    world_file = red.get("world").decode()

    world = World(world_file)

    while True:
        item = red.brpop("tasks")[1]
        try:
            id, sched = pickle.loads(item)
            print(f"recieved : {id}")
            val = world.simulate(sched)
            red.rpush("results",f"{id} {val}")
        except KeyboardInterrupt:
            red.lpush("tasks", item)
            break
