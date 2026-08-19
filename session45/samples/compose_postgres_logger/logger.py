import os
import time
from datetime import datetime

import psycopg


def get_connection():
    conninfo = (
        f"host={os.getenv('POSTGRES_HOST', 'db')} "
        f"port={os.getenv('POSTGRES_PORT', '5432')} "
        f"dbname={os.getenv('POSTGRES_DB', 'logsdb')} "
        f"user={os.getenv('POSTGRES_USER', 'user')} "
        f"password={os.getenv('POSTGRES_PASSWORD', 'password')}"
    )

    for attempt in range(1, 16):
        try:
            return psycopg.connect(conninfo)
        except psycopg.OperationalError:
            print(f"PostgreSQL is not ready yet. Retry {attempt}/15...", flush=True)
            time.sleep(1)

    raise RuntimeError("Could not connect to PostgreSQL")


def main():
    message = f"postgres log created at {datetime.now().isoformat(timespec='seconds')}"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS logs "
                "(id SERIAL PRIMARY KEY, message TEXT NOT NULL, created_at TIMESTAMP DEFAULT NOW())"
            )
            cur.execute("INSERT INTO logs (message) VALUES (%s)", (message,))

    print(message, flush=True)


if __name__ == "__main__":
    main()
