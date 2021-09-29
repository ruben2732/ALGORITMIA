#!/usr/bin/env python3
import time
from funcion_predefinida import *

for n in [10, 100, 1000, 10000, 100000, 1000000]:
    test = f"nums/nums{n}"
    f = open(test)
    nums = read_data(f)
    t0 = time.perf_counter()
    m = process(nums)
    t1 = time.perf_counter()
    print (f"{test+':':18} {t1-t0:f}")