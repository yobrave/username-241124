"""Entrant's own make.fun handle, shipped as the whole entry.

The handle is the payload. The program stamps it into the output
folder, hashes both sides of the trip, and refuses to bow if the
digests disagree.
"""
import hashlib
import os

HANDLE = "yobrave-lee"
STAMP_NO = "rr-1125-02"


def ship(base):
    base = base or "output"
    os.makedirs(base, exist_ok=True)
    p = os.path.join(base, "entry.txt")
    payload = HANDLE + "\n"
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(payload)
    with open(p, "rb") as f:
        blob = f.read()
    want = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    have = hashlib.sha256(blob).hexdigest()
    assert want == have, "handle checksum drifted"
    return blob.decode("utf-8").strip()


got = ship(os.environ.get("MAKEFUN_OUTPUT_DIR"))
assert got == HANDLE
print("handle shipped:", got, "| stamp:", STAMP_NO)
