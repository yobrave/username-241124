import json
import os

TAG_USR = "usr3-handle"
WIDTH = 30


def handle(raw_bytes):
    for row in raw_bytes.splitlines():
        if row.strip():
            return row.strip().decode("utf-8")
    return ""


def check_handle(name):
    return bool(name) and name == name.strip() and len(name) <= WIDTH


def sign_in(name, root):
    gate = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(gate, exist_ok=True)
    badge = os.path.join(gate, "entry.txt")
    ink = name.encode("utf-8")
    with open(badge, "wb") as engraver:
        engraver.write(ink)
    if open(badge, "rb").read() != ink:
        raise RuntimeError("badge misprinted")
    return badge


root = os.path.dirname(os.path.abspath(__file__))
name = handle(open(os.path.join(root, "entry.txt"), "rb").read())

if not check_handle(name):
    print(json.dumps({"handle": "anonymous", "size": len(name)}))
    raise SystemExit(1)
badge = sign_in(name, root)
print(json.dumps({"handle": name, "size": len(name), "width": WIDTH, "tag": TAG_USR, "badge": os.path.basename(badge)}))
