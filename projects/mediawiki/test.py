import multiprocessing
import time

class MyFancyClass(object):
    
    def __init__(self, name):
        self.name = name
        self._queue = multiprocessing.Queue()
        self.add(printfunctionname)
    
    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print 'Doing something fancy in %s for %s!' % (proc_name, self.name)

    def add(self, function):
        self._queue.put(function)
        
    def theMagic(self):
        
        
        p = multiprocessing.Process(target=worker, args=(self._queue,))
        p.start()
        print self._queue.qsize()
        time.sleep(1.5)
        print self._queue.qsize()
        # Wait for the worker to finish
        self._queue.close()
        self._queue.join_thread()
        p.join()
        
def worker(q):
    time.sleep(1)
    myFunction = q.get()
    print "removed from _queue"
    #TODO: Add Error trapping
    myFunction()
    time.sleep(1)

def printfunctionname():
    print printfunctionname.__name__
    time.sleep(1)

if __name__ == '__main__':
    mahClass = MyFancyClass("name")
    mahClass.theMagic()