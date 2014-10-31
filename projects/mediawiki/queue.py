class Queue:
    """An asynchronous queuing library."""
    
    _parallelism = 1
    _size = 0
    _inFlight = 0
    _tasks = []
    
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
        return self._size
        
    def isRunning(self):
        #* @returns {Boolean} Whether the queue is running or not.
        
        return False
    
    def inFlight(self):
        #* @returns {Number} Number of tasks currently executing.
        
        return self._inFlight
        
    def addTask(self, function):
        # * Adds a new task to the queue. When executed, the task will be passed a callback used to signal the task has completed:
        # *
        # * task(callback)
        # *
        # * @param {Function} task Function which begins the asynchronous task,
        # * taking a callback to be invoked upon task completion.
        # * @returns The queue object.
        self._tasks.append(function)
        self._size += 1
        
        