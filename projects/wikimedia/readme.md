The Task:

Your task is to write an asynchronous queuing library. You can write this task in the language of your choice.

The code that illustrates the description of the task should be understood like pseudo-code.

The task should occupy you about 3 hours; try to use as few additional high level libraries as possible. Keep things simple and concentrate on fulfilling the API contract, the queue should not need a storage layer.

The following signatures explain the semantics you must fulfill, but feel free to add additional features that you feel are pragmatic, elegant, or awesome opportunities to show off. When you're ready, please send your solution to us in a file, not hosted on github.

Constructor
/**
* Constructs a new Queue.
* @constructor
* @param {Number} [parallelism=1] Maximum number of tasks to run in parallel;
* cannot be less than 1 or an error is raised.
* @returns {Queue} A new queue object.
*/
Queue(parallelism){}

Instance Methods
Given:
q = Queue();

...the Queue object q should have the following interface:
/**
* @returns {Number} Number of tasks awaiting execution. Does not count any tasks that
* are in-flight.
*/
q.size()
/**
* @returns {Boolean} Whether the queue is running or not.
*/
q.isRunning()

/**
* @returns {Number} Number of tasks currently executing.
*/
q.inFlight()

/**
* Adds a new task to the queue. When executed, the task will be passed a callback used to signal the task has completed:
*
* task(callback)
*
* @param {Function} task Function which begins the asynchronous task,
* taking a callback to be invoked upon task completion.
* @returns The queue object.
*/
q.addTask(task)

/**
* Adds a callback to be invoked when all tasks have been completed:
*
* callback.call(queue)
*
* @param {Function} callback Function to invoke when all tasks have completed;
* it will be passed the queue object.
* @returns The queue object.
*/
q.addCallback(callback)

/**
* Begin executing queued tasks.
*
* Queued tasks execute in order queued, but tasks do not wait for prior tasks
* to complete -- this implies the order of task completion is undefined. No more
* than `parallelism` tasks will run at once.
*
* Queue will continue executing tasks until all have completed, at which point it
* executes all registered callbacks. Calling `start` repeatedly while the queue is
* running has no effect (though the queue can be started again with new tasks once
* it completes).
*
* @returns The queue object.
*/
q.start()

Notes
The queue offers no error-handling or propagation -- this is up to the programmer -- but it should not fail or stop execution due to task errors. The same is true of callbacks.
