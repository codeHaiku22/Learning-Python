#!/usr/bin/python3
import time

start = time.time()

time.sleep(2)

stop = time.time()

elapsed = stop - start

print("Total elapsed time:", float(elapsed), "seconds.")
print("Total elapsed time:", int(elapsed), "seconds.")