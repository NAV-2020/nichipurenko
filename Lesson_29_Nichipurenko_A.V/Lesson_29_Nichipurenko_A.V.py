"""
import asyncio

async def foo():
    print("I am foo")
    await asyncio.sleep(0)
    print("I am foo too")

async def bar ():
    print("I am bar")
    await asyncio.sleep(0)
    print("I am bar too")


loop = asyncio.get_event_loop()
tasks = [loop.create_task(foo()), loop.create_task(bar())]

wait_tasks = asyncio.wait(tasks)
loop.run_until_complete(wait_tasks)
loop.close()


import asyncio
import aiohttp
import time
import random



URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


async def fetch_async(pid):
    start = time.time()
    sleepy_time = random.randint(2, 5)
    print(f'Fetch process {pid}, asleep for {sleepy_time}')
    await asyncio.sleep(sleepy_time)


    async with aiohttp.request('GET', URL) as response:
        datetime = response.headers.get('Date')
    return f'Process {pid}:{datetime}, took: {time.time() - start} seconds'


async def asynchronus():
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        print(f'>>*{i + 1} {result}')
    print(f'Process took: {time.time() - start} seconds')



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asynchronus())
    loop.close()

    
    
import time
import random
from threading import Thread
 
def random_delay():
    return random.random() * 5
 
def random_countdown():
    return random.randrange(5)
 
def launch_rocket(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        time.sleep(1)
    print("Rocket launched")
 
def rockets():

    n = 10_000
    return ((random_delay(), random_countdown())
        for _ in range(n)
        )
 
def run_threades():
    threads =[
        Thread(target=launhc_rocket, args=(d, c))
        for d, c in rockets()
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    for d, c in rockets():
        launch_rocket(d, c)


"""

import time
import random
from threading import Thread
from enum import Enum, auto
import heapq
 
def random_delay():
    return random.random() * 5
 
def random_countdown():
    return random.randrange(5)
 
def launch_rocket(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        time.sleep(1)
    print("Rocket launched")
 
def rockets():
    n = 10_000
    return [
        (random_delay(), random_countdown())
        for _ in range(n)
        ]
 
def run_threads():
    threads = [
        Thread(target=launch_rocket, args=(d, c))
        for d, c in rockets()
        ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
 
class State(Enum):
    COUNTING = auto()
    WAITING = auto()
    LAUNCHING = auto()
 
class Op(Enum):
    WAIT = auto()
    STOP = auto()
 
class Launch:
    def __init__(self, delay, countdown):
        self._state = State.WAITING
        self._delay = delay
        self._countdown = countdown
 
    def step(self):
        if self._state is State.WAITING:
            self._state = State.COUNTING
            return Op.WAIT, self._state

        if self._state is State.COUNTING:
            if self._countdown == 0:
                self._state = State.LAUNCHING
            else:
                print(f"{self._countdown}...")
                self._countdown -= 1
                return Op.WAIT, 1

        if self._state is State.LAUNCHING:
            print("Rocker launched!")
            return Op.STOP, None
            assert False, self._state
 
def now():
    return time.time()
 
def run(rockets):
    start = now()
    work = [(start, i, Launch(d, c))
            for i, (d, c) in enumerate(rockets)]

    while work:
        step_at, id, launch = heapq.heappop(work)
        wait = step_at - now()
        if wait > 0:
            time.sleep(wait)
        op, arg = launch.step()
        if op == Op.WAIT:
            step_at = now()
            heapq.heappush(work, (step_at, id, launch))
        else:
            assert op is Op.STOP
 
if __name__ == "__main__":
     # run_threads()
    run(rockets())