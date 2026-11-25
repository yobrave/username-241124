"""Username badge engraver: engraves the handle, clips it onto the output lanyard."""
STAMP = "onebug-11251142-usr3"
import json
import os
from pathlib import Path

LANYARD = Path(__file__).resolve().parent
CLIP_MAX = 30
BADGE = "yobrave"


def engrave():
    plate = LANYARD / "entry.txt"
    carving = plate.read_text(encoding="utf-8").strip()
    etched = 1 <= len(carving) <= CLIP_MAX
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and etched:
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(plate.read_bytes())
    print(json.dumps({"etched": etched, "stamp": STAMP, "carving": len(carving), "clip_max": CLIP_MAX}))


if __name__ == "__main__":
    engrave()
