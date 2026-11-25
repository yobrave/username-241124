"""usr6: nameplate etcher. Etches the entrant's own handle onto the tray."""
import json
import os
import sys
from pathlib import Path

PLATE = 30
HANDLE_HINT = "single word, no spaces"


def etch(root: Path, tray: Path) -> dict:
    raw = root.joinpath("entry.txt").read_text(encoding="utf-8")
    name = raw.strip()
    carved = name != "" and len(name) <= PLATE and not name.isspace() and len(name.split()) == 1
    if carved:
        tray.mkdir(parents=True, exist_ok=True)
        (tray / "entry.txt").write_bytes(name.encode("utf-8"))
    return {"etched": carved, "name_len": len(name), "plate": PLATE, "hint": HANDLE_HINT, "shop": "usr6-etcher-r11251422"}


def main():
    tray = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    report = etch(Path(__file__).resolve().parent, tray)
    print("VERDICT", json.dumps(report))
    return 0 if report["etched"] else 1


if __name__ == "__main__":
    sys.exit(main())
