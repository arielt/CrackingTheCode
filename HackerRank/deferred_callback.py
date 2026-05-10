# Given set_call and get_time, implement add_call for multiple timers.
# Call of set_call will override currently scheduled callback.

import heapq
import threading
import time

class MySystem:
    def __init__(self):
        self.q = []

    def set_call(self, delay, callback):
        # not a full implementation
        print "delay ", delay
        if delay > 0:
            time.sleep(delay/1000)
        t = threading.Thread(target=callback)
        t.start()

    def get_time(self):
        return int(time.time()*1000.0)

    def my_run(arg):
        print "run invoked ", arg

    def add_call(self, delay, callback):
        now = self.get_time()
        heapq.heappush(self.q, (now + delay, callback))
        (next_time, next_callback) = self.q[0]
        print next_time, next_callback
        self.set_call(next_time - now, self.my_run)

def call_me():
    print "called me ", int(time.time()*1000.0)
    print ""

t = threading.Thread(target=call_me)
t.start()

ms = MySystem()
ms.add_call(5000, call_me)
ms.add_call(1000, call_me)

