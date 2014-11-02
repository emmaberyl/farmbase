import multiprocessing
import time

class Queue:
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
        self._isRunning = False
    
    def size(self):
        #* @returns {Number} Number of tasks awaiting execution. Does not count any tasks that are in flight
        return len(self._tasks.qsize())
        
    def isRunning(self):
        #* @returns {Boolean} Whether the queue is running or not.
        
        return self._isRunning
    
    def inFlight(self):
        #* @returns {Number} Number of tasks currently executing.
        
        return len(self._jobs.qsize())
        
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
        if self._isRunning:
            return
        
        #fire up our processes
        for x in range(1, self._parallelism):
            p = multiprocessing.Process(target = self.startJobs, args=(self._isRunning,))
            p.start()
        
        #this is done in a process so that we can query the status of the queue asynchronously
        p = multiprocessing.Process(target = self.startJobs, args=(self._isRunning,))
        p.start()
    
    def startJobs(self, _isRunning):
        # function for executing jobs asynchronously
        _isRunning = True
        
        while len(self._tasks) > 0:
        
            p = multiprocessing.Process(target = self._tasks.pop(0))
            self._jobs.append(p)
            p.start()
            
            # wait until a parallel job  becomes available
            while len(self._jobs) >= self._parallelism:
                #let's wait a bit to give them a chance to finish
                time.sleep(1)
                
                # check if any of the jobs are finished
                for (i, job) in enumerate(self._jobs):
                    if not job.is_alive():
                        # this job is finished, remove it from our inflight jobs
                        self._jobs.pop(i)

        self._isRunning = False