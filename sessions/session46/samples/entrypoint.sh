#!/bin/sh
set -e

if [ -n "$WAIT_FOR_DB_HOST" ]; then
    DB_PORT="${WAIT_FOR_DB_PORT:-5432}"
    echo "Waiting for database at $WAIT_FOR_DB_HOST:$DB_PORT..."
    python - <<'PY'
import os
import socket
import time

host = os.environ["WAIT_FOR_DB_HOST"]
port = int(os.environ.get("WAIT_FOR_DB_PORT", "5432"))

while True:
    try:
        with socket.create_connection((host, port), timeout=2):
            break
    except OSError:
        print("Database is not ready yet; waiting...")
        time.sleep(1)
PY
fi

if [ "$RUN_MIGRATIONS" = "1" ]; then
    echo "Running database migrations..."
    python manage.py migrate
fi

if [ "$COLLECT_STATIC" = "1" ]; then
    echo "Collecting static files..."
    python manage.py collectstatic --noinput
fi

exec "$@"
