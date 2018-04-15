import sys
import os

# add the location of search_local.py to sys.path
file_dir = (os.path.dirname(os.path.abspath(__file__)))
rel_path = ("../../scripts")
sys.path.insert(0, os.path.join(file_dir, rel_path))

import search_local
