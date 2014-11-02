import multiprocessing
import time

# TODO: Callback?  Don't really understand the requirement.

class MyQueue:
    """An asynchronous queuing library."""
    
    def __init__(self, parallelism=1):
    #* Constructs a new Queue.
    #* @constructor
    #* @param {Number} [parallelism=1] Maximum number of tasks to run in parallel;
    # cannot be less than 1 or an error is raised.
    # @returns {Queue} A new queue object.
        if (parallelism < 1):
            raise Exception("parallelism cannot be less than 1")
            
        self._parallelism = parallelism
        self._tasks = multiprocessing.Queue()
        self._jobs = multiprocessing.Queue()
        self._isRunning = multiprocessing.Value('b', False)
    
    def size(self):
        #* @returns {Number} Number of tasks awaiting execution. Does not count any tasks that are in flight
        return self._tasks.qsize()
        
    def isRunning(self):
        #* @returns {Boolean} Whether the queue is running or not.
        
        return self._isRunning.value
    
    def inFlight(self):
        #* @returns {Number} Number of tasks currently executing.
        
        return self._jobs.qsize()
        
    def addTask(self, function):
        # * Adds a new task to the queue. When executed, the task will be passed a callback used to signal the task has completed:
        # *
        # * task(callback)
        # *
        # * @param {Function} task Function which begins the asynchronous task,
        # * taking a callback to be invoked upon task completion.
        # * @returns The queue object.
        self._tasks.put(function)
        
    def start(self):
        # * Begin executing queued tasks.
        # *
        # * Queued tasks execute in order queued, but tasks do not wait for prior tasks
        # * to complete -- this implies the order of task completion is undefined. No more
        # * than `parallelism` tasks will run at once.
        # *
        # * Queue will continue executing tasks until all have completed, at which point it
        # * executes all registered callbacks. Calling `start` repeatedly while the queue is
        # * running has no effect (though the queue can be started again with new tasks once
        # * it completes).
        # *
        # * @returns The queue object.
        
        # don't don't don't let's start #tmbg
        # don't start if we've started
        if self._isRunning.value:
            return
        
        self._isRunning.value = True
        #fire up our processes
        for x in range(0, self._parallelism):
            
            p = multiprocessing.Process(target=self.worker, args=(self._tasks, self._jobs, self._isRunning))
            
            p.start()

    def worker(self, tasksQueue, jobsQueue, isRunning):
                    
        while (tasksQueue.qsize() > 0):
            #potential race condition between multiple processors
            try:
                myFunction = tasksQueue.get()
            except (Queue.Empty):
                break;
            # we're tracing this for the ability to count inflight jobs
            # the actual value here is inconsequential, but may be useful if you wanted to poll your queue
            jobsQueue.put(myFunction)
            
            try:
                myFunction()
                #remove something from the jobs queue after complete.  Doesn't really matter what we're just using this as a counter
                jobsQueue.get()
            except:
                # maybe add some logging here?
                pass
            
        if (tasksQueue.qsize() == 0 and jobsQueue.qsize() == 0):
            isRunning.value = False
    
    # def __del__(self):
        # self._tasks.close()
        # self._jobs.close()
        