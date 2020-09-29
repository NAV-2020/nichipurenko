import sys
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
    yield from sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        yield from sleep(1)
    print("Rocket launched")
 
def rockets():
    n = 10_000
    return [
        (random_delay(), random_countdown())
        for _ in range(n)
    ]
 
def run_threads(rockets):
    threads = [
        Thread(target=launch_rocket, args=(d, c))
        for d, c in rockets
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
 
def sleep(delay):
    yield Op.WAIT, delay
 
class Op(Enum):
    WAIT = auto()
    STOP = auto()
 
def now():
    return time.time()
 
def run(rockets):
    start = now()
    work = [(start, i, launch_rocket(d, c))
            for i, (d, c) in enumerate(rockets)]
 
    while work:
        step_at, id, launch = heapq.heappop(work)
        wait = step_at - now()
        if wait > 0:
            time.sleep(wait)
        try:
            op, arg = launch.send(None)
        except StopIteration:
            continue
        if op == Op.WAIT:
            step_at = now()
            heapq.heappush(work, (step_at, id, launch))
        else:
            assert op is Op.STOP
 
if __name__ == "__main__":
    if sys.argv[1] == 'threading':
        run_threads(rockets())
    else:
        run(rockets())