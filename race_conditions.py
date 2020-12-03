#!/usr/bin/python

#Race Conditions
"""
Race conditions are an entire class of subtle bugs that can and frequently do happen in mult-threaded code.
They occur because the programmer hasn't sufficiently protecte data access to prevent threads from interefering with each other.
You need to take extra steps when writing threaded code to ensure things are thread-safe.
The OS controls when a thread runs and when it gets swapped out to let another thread run. 
 - This can occur at any point, even while doing sub-steps of a Python statement.
"""

#Each thread in accesses the same global variable.
#To increment the counter, each thread needs to read the current value, add 1 to it, and save that value back tot he variable.
#The OS knows nothing about the code and can swap threads at any point in the execution.
# - It is possible that the swap can occur after a thread has read the value, but before it has incremented it and written it back.
# - If the new code that is running modified counter as well, then the first thread has a stale copy of the data - trouble!
#This condition is rare and the code below can be run thouands of times without encountering an issue.
# - However, when the issue occurs, it is very difficult to debug (since it is hard to faithfully reproduce).
import concurrent.futures

counter = 0

def increment_counter(fake_value):
    global counter
    for _ in range(100):
        counter += 1

if __name__ == "__main__":
    fake_data = [x for x in range(5000)]
    print(fake_data)
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
        executor.map(increment_counter, fake_data)