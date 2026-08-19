import time


def main():
    counter = 1
    while True:
        print(f"Worker tick {counter}", flush=True)
        counter += 1
        time.sleep(5)


if __name__ == "__main__":
    main()
