import sys
from pathlib import Path

DIR = Path(__file__).resolve()
print(DIR)
ROOT_DIR = DIR.parents[2]
print(ROOT_DIR)

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
