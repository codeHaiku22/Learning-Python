#!/usr/bin/python3

#time
import time

start = time.time()

time.sleep(2)

stop = time.time()

elapsed = stop - start

print(elapsed)
print("Total elapsed time:", float(elapsed), "seconds.")
print("Total elapsed time:", int(elapsed), "seconds.")

#timeit
import timeit

start = timeit.default_timer()

time.sleep(2)

stop = timeit.default_timer()

elapsed = stop - start

print(elapsed)
print("Total elapsed time:", float(elapsed), "seconds.")
print("Total elapsed time:", int(elapsed), "seconds.")