import sys


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "Docker Student"
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
