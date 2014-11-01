import multiprocessing
import time

class Queue:
    """An asynchronous queuing library."""
    
    _parallelism = 1
    _tasks = []
    _jobs = []
    _isRunning = False
    
    def __init__(self, parallelism):
    
    #* Constructs a new Queue.
    #* @constructor
    #* @param {Number} [parallelism=1] Maximum number of tasks to run in parallel;
    # cannot be less than 1 or an error is raised.
    # @returns {Queue} A new queue object.
        if (parallelism < 1):
            raise Exception("parallelism cannot be less than 1")
            
        self._parallelism = parallelism
    
    def size(self):
        #* @returns {Number} Number of tasks awaiting execution. Does not count any tasks that are in flight
        return len(self._tasks)
        
    def isRunning(self):
        #* @returns {Boolean} Whether the queue is running or not.
        
        return self._isRunning
    
    def inFlight(self):
        #* @returns {Number} Number of tasks currently executing.
        
        return len(self._jobs)
        
    def addTask(self, function):
        # * Adds a new task to the queue. When executed, the task will be passed a callback used to signal the task has completed:
        # *
        # * task(callback)
        # *
        # * @param {Function} task Function which begins the asynchronous task,
        # * taking a callback to be invoked upon task completion.
        # * @returns The queue object.
        self._tasks.append(function)
        
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
        
        self._isRunning = True
        
        while len(self._tasks) > 0:
        
            p = multiprocessing.Process(target = task.pop())
            jobs.append(p)
            p.start()
            
            # wait until a parallel job  becomes available
            while len(_jobs) >= self._parallelism:
                #let's wait a bit to give them a chance to finish
                time.sleep(1)
                
                # check if any of the jobs are finished
                for (i, job) in enumerate(jobs):
                    if not job.is_alive():
                        # this job is finished, remove it from our inflight jobs
                        jobs.pop(i)

        self._isRunning = False
        