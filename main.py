"""One letter for the day: Z, as in zombie. Bad sleep, slow shuffle, coffee hunt all day."""
from pathlib import Path

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(b"Z")
