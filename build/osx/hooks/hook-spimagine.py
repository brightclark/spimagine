from __future__ import print_function


import sys
import os
sys.path.append(os.path.split(os.path.abspath(__file__))[0])
from hook_utils import _my_collect_data_files

datas = _my_collect_data_files("spimagine", flatten_dirs = True)


print("\n"*5)
print(datas)
print("\n"*5)
