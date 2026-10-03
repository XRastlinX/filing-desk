"""One landing and one refusal. A landing is not a proof."""
from acthive import Hive

def main() -> None:
    hive = Hive()
    land = hive.file("elegxis", "elegxis")
    refuse = hive.file("biaschisis", "leiorrhoe")
    print(f"land {land.requested} -> {land.landed}: {land.verdict}")
    print(f"refuse {refuse.requested} -> {refuse.landed}: {refuse.verdict}")

if __name__ == "__main__":
    main()
