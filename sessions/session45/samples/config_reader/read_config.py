import json
from pathlib import Path


def main():
    config_path = Path("config.json")
    config = json.loads(config_path.read_text())

    print(f"App name: {config['app_name']}")
    print(f"Environment: {config['environment']}")
    print(f"Debug: {config['debug']}")
    print(f"Version: {config['version']}")


if __name__ == "__main__":
    main()
