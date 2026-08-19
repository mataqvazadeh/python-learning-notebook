import os
import time
from datetime import datetime

import redis


def get_client():
    host = os.getenv("REDIS_HOST", "redis")
    port = int(os.getenv("REDIS_PORT", "6379"))

    for attempt in range(1, 11):
        try:
            client = redis.Redis(host=host, port=port, decode_responses=True)
            client.ping()
            return client
        except redis.RedisError:
            print(f"Redis is not ready yet. Retry {attempt}/10...", flush=True)
            time.sleep(1)

    raise RuntimeError("Could not connect to Redis")


def main():
    client = get_client()
    message = f"log created at {datetime.now().isoformat(timespec='seconds')}"
    client.rpush("logs", message)
    print(message, flush=True)


if __name__ == "__main__":
    main()
