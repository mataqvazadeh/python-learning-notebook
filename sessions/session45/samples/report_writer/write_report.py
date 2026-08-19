from datetime import datetime
from pathlib import Path


def main():
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    report_path = output_dir / "report.txt"
    report_path.write_text(
        "Docker report\n"
        f"Generated at: {datetime.now().isoformat(timespec='seconds')}\n"
        "Status: success\n"
    )

    print(f"Report written to {report_path}")


if __name__ == "__main__":
    main()
