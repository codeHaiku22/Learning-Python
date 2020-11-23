#!/usr/bin/python

#Concurrency and Parallelism
#The asyncio library is like any other and can be imported into a code page.
# - It allows for the ability to write concurrent code using the async/await syntax.

#A process is a program that has been loaded into memory along with all of the resources it needs to operate.
# - A process has its own memory space.

#A thread is the unit of execution within a process.  
# - A process can have multiple threads running where each thread uses the process's memory space and shares it with other threads.

#Multi-threading is a technique where multiple threads are spawned by a process to do different tasks at approximately the same time (one after the other).
# - This gives the illusion that the threads are running in parallel, when actually they are running concurrently.
# - In Python the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.

#Multi-threading and asycnio run on a single processor and therefore only run one-at-a-time.
# - In threading, the OS actually knows about each thread and can interrrupt it to start running a different thread.
#    + This is called pre-emptive multitasking since the OS can pre-emp a thread to make a switch.
#    + The code in the thread doesn't need to do anything to make the switch.
# - With asyncio the tasks must cooperate by announcing when they are ready to be switched out.
#    + This is called cooperative multitasking and allows you to control where your task will be swapped out.
#    + The code int he task has to change slightly to make this happen. 

#Multiprocessing is a technique where parallelism in its truest form is achieved.
# - Multiple processes are run across multiple CPU cores which do not share the resources among them.
# - Each process can have multiple threads running in its own memory space.
# - Each process has its own instanec of the Python interpreter doing the job of executing the instructions.

#I/O-Bound Process
# - Program spends most of its time talking to a slow device (network connection, hard drive, printer).
# - Speeding it up involves overlapping the times spent waiting for these devices.

#CPU-Bound Process
# - Program spends most if its time doing CPU operations.
# - Speeding it up involves finding ways to do more computations in the same amount of time.


#How to Speed Up an I/O-Bound Program
#Let's look at a common problem of downloading content over the network by downloading web pages from a few sites.

#Synchronous Version
"""
A non-concurrent version of this task
PROS (+)
 - Simple write the code and debug
CONS (-)
 - Relatively slow compared to other solutions
"""
import requests
import time

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds.")                                        #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Downloaded 20 in 1.1254007816314697 seconds.

#Threading Version
"""
A threaded version of this task
Uses the ThreadPoolExecutor creates and manages a concurrent pool of threads determining how and when each thread runs.
 - The map() method runs the passed in function on each of the sites in the list, concurrently using the pool of threads it is managing.
Although not present, the Thread.start(), Thread.join(), and Queue can be used to achieve fine control of how threads are run.
 - Starting with Python 3.2, Executors were introduced to manage the details if fine control is not needed.
Note that each thread needs its own separate session and this is accomplished with requests.Session() object.
Since the OS is in control of when this task gets interrupted and another task starts, any data shared between threads needs to be protected (thread-safe).
 - requests.Session() as used in the example above is not thread-safe.
 - The ThreadPoolExecutor objects ensures that the we are thread-safe.
 - Also, Threading.local() and get_session()creates an object that looks global but is specific to each individual thread.
PROS (+)
 - Multiple threads with open requests to web sites at the same time allows for overlapping wait times.
 - Fast!
CONS (-)
 - More code
 - More considerations needed especially with what data is shared between threads.
 - Threads can ineract is ways that are subtle and hard to detect causing race conditions - random, intermittent bugs that are difficult to find.
"""
import requests
import time
import concurrent.futures
import threading

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds.")                                        #Read 10394 from https://www.jython.org
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 10394 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Downloaded 20 in 0.3713233470916748 seconds.

#asyncio Version
"""
In asyncio, a single Python object called the event loop controls how and when each task gets run.
 - The event loop is aware of each task and the state of the task
 - It maintains a list of tasks and the state they are in
 - The event loops begins a task that is ready to run and puts the task in complete control until it hands control back to the event loop.
 - The task is put into the proper list based on its status and picks another task to run (the one that has been waiting the longest).
 - Tasks never give up control without intentionally doing so.
 - Tasks are never interuppted in the middle of an operation.
Code doesn't have to be written to be thread-safe.
async and await
 - await allows the task to hand control back to the event loop.
 - async is like a flag to Python telling it that the fuction about to be defined uses await (execept with asynchoronous generators)
 - Any function that calls await needs to be marked with async.
The async with statement creates a context manager from an object you would normally await.
 - The idea is to flag this context manager as something that gets swapped out.
A context manager is created in the download_all_sites code block.
 - A list of tasks is created using using the asyncio.ensure_future() method which also starts the tasks.
 - Once all tasks are created, this function uses asyncio.gather() to keep the session context alive until all tasks have completed.
PROS (+)
 - Very fast!
 - Running the asyncio version with hundreds of tasks didn't cause any slowdown.
    + It scales far better than threading since each task takes fewer resources and less time to create than a thread.
CONS (-)
 - The asyncio and aiohttp libraries are needed.
 - All advantages of cooperative multitasking are negated if one of the tasks doesn't cooperate.
    + A coding mistake can cause a task to run off and hold the processor for a long time.
    + The event loop cannot break in if a task does not hand control back to it.
"""
import time
import asyncio
import aiohttp

async def download_sites(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_sites(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds.")                                        #Read 3586 from https://www.jython.org
                                                                                                    #Read 3586 from https://www.jython.org
                                                                                                    #Read 3586 from https://www.jython.org
                                                                                                    #Read 3586 from https://www.jython.org
                                                                                                    #Read 3586 from https://www.jython.org
                                                                                                    #Read 3586 from https://www.jython.org
                                                                                                    #Read 3586 from https://www.jython.org
                                                                                                    #Read 3586 from https://www.jython.org
                                                                                                    #Read 3586 from https://www.jython.org
                                                                                                    #Read 3586 from https://www.jython.org
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Downloaded 20 in 0.18891167640686035 seconds.

#multiprocessing Version
"""
Unlike the versions above, the multiprocessing version takes full advantage of the multiple CPUs of the host PC.    
 - It does this by creating a new instance of the Python interpreter to run on each CPU and then farming out part of this program to run on it.
The download_all_sites() code block creates a multiprocessing.Pool object which maps download_site to the iterable sites.
 - The pool creates a number of separate Python interpreter processes and runs each one the specified number of times in the iterable (list of sites).
 - The communication between the main process and the other processes is handled bu the multiprocessing module.
 - The multiprocessing.Pool line of code does not specify how may processes to create in the pool, although that is an optional parameter.
    + By default, the multiprocessing.Pool object determines the number of CPUs in the host PC and matches that.
The inilaizer=set_global_session creates a session for each process.
 - Recall that each process in our Pool has its own memory space and cannot share things like a Session object.
    + This is why we cannot create a new Session each time.
The initializer function parameter is built for just this case.
 - There is no way to pass a return value back from the initializer to the function called by the download_site() process, but you can initialize a global session variable.
    + This variable holds the single session for each process.
    + Because each process has its own memory space, the global for each one will be different.    
 PROS (+)
 - Relatively easy to set up.
 - Requires little extra code
 - Takes advantage of the CPU power in the host PC
 CONS (-)
 - Requires extra setup.
 - The global session object is strange
 - You have to think about which variables will be accessed in earch process.
 - Slower than asyncio version and threading version.
    + The cost of for setting up and tearing down all of those processes was larger than teh benefit of doing the I/O requests in parallel.
"""
import requests
import time
import multiprocessing

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds.")                                        #ForkPoolWorker-2:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-1:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-4:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-3:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-2:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #ForkPoolWorker-1:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #ForkPoolWorker-2:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-4:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #ForkPoolWorker-1:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-3:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #ForkPoolWorker-4:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-3:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-1:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #ForkPoolWorker-2:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #ForkPoolWorker-2:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-1:Read 10394 from https://www.jython.org
                                                                                                    #ForkPoolWorker-4:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #ForkPoolWorker-3:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #ForkPoolWorker-1:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #ForkPoolWorker-2:Read 277 from http://olympus.realpython.org/dice
                                                                                                    #Downloaded 20 in 0.5544731616973877 seconds.


#How to Speed Up a CPU-Bound Program
#Let's look at a function to create something that takes a long time to run on the CPU.
# - This function computers the sum of the squares of each number from 0 to the passed-in value.

#Non-concurrent Version
"""
A non-concurrent version of this task
PROS (+)
 - Simple write the code and debug
CONS (-)
 - Relatively slow compared to other solutions
"""
import time

def sum_of_squares(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    for number in numbers:
        sum_of_squares(number)    

if __name__ == "__main__":
    numbers = [5000000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration in seconds: {duration}")                                                       #Duration in seconds: 7.780023097991943

#multiprocessing Version
"""
The multiprocessing capability in Python is explicitly designed to share heavy CPU workloads across multiple CPUs.
Little of the original code has beenchanged from looping through the numbers to creating a multiprocessing.Pool object and using its .map() method.
The processes optional parameter to the multiprocessing.Pool() constructor deserves some attention.
 - You can specify how many Process objects you want created and managed in the pool.
 - By default, it will determine how many CPUs are in your machine and create a process for each one.
 - For this example, it worked out well.  However in a Production environment, it is good to have control.
PROS (+)
 - Relatively easy to setup
 - Requires little extra code
 - Takes full advantage of the CPU power in the host PC
CONS (-)
 - Splitting your problem up so each processor can work independently can be difficult.
 - Many solutions require some communication between the processes.
    + This can add complexity to a solution that a non-concurrent program would not need to deal with.
"""    
import time
import multiprocessing

def sum_of_squares(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(sum_of_squares, numbers)

if __name__ == "__main__":
    number = [5000000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration in seconds: {duration}")                                                       #Duration in seconds: 2.7579636573791504


#When to Use Concurrency
#Only use concurrency if you have a known performance issue and then determine which type of concurrency is needed (I/O-bound or CPU-bound).
# - I/O-bound programs are those that spend most of their time waiting for something to happen.
# - CPU-bound programs spend their time processing data or crunching numbers as fast as they can.
#For I/O-bound problems, there a general rule of thumb in the Python community: "Use asyncio when you can, threading when you must."
# - asyncio can provide the best speed up for this type of program, but it requires critical libraries be imported to take advantage of asyncio.
# - Any task that doesn't give up control to the event loop will block all of the other tasks.