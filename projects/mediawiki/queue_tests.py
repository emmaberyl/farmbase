import unittest
from myqueue import MyQueue
import time
from datetime import datetime
import os

class QueueTests(unittest.TestCase):
    # test class for MyQueue
    # Note: 
    #        this script jams some non-critical warnings. I believe this is a bug in python (http://bugs.python.org/issue14548)
    #         Warning:   Exception AssertionError: AssertionError() in <Finalize object, dead> ignored
    def testConstructor(self):
        q = MyQueue()
        self.assertEqual(1, q._parallelism)
        
        self.assertRaises(Exception, MyQueue, 0)
        self.assertEqual(0, q.size())
        self.assertFalse(q.isRunning())
        self.assertEqual(0, q.inFlight())
        
    
    def testStartSimple(self):
        #should be able to run 2 tasks serially in about 2 seconds
        startTime = datetime.now()
        
        q = MyQueue()
        q.addTask(waitOneSecond)
        q.addTask(waitOneSecond)
        
        q.addCallback(callbackFunc)
        
        q.start()
        
        self.sleepCountAssert(startTime, q, 2)
        # callback function creates this file.  testing for a file existence is an easy way of passing info between multithreaded tasks
        self.assertTrue(os.path.isfile("callback.txt"))
        os.system("rm callback.txt")
    
    def testStartComplex(self):
        q = MyQueue()
        
        q.addTask(waitOneSecond)
        q.addTask(waitFiveSeconds)
        q.addTask(waitOneSecond)
        self.assertEqual(3, q.size())
        self.assertFalse(q.isRunning())
        self.assertEqual(0, q.inFlight())
        
        q.start()
        
        time.sleep(.5)
        self.assertTrue(q.isRunning())
        self.assertEqual(1, q.inFlight())
        self.assertEqual(2, q.size())
        
        time.sleep(1)
        self.assertEqual(1, q.inFlight())
        self.assertEqual(1, q.size())
        self.assertTrue(q.isRunning())
        
        time.sleep(5)
        self.assertEqual(1, q.inFlight())
        self.assertEqual(0, q.size())
        self.assertTrue(q.isRunning())
        
        time.sleep(1)
        self.assertEqual(0, q.inFlight())
        self.assertEqual(0, q.size())
        self.assertFalse(q.isRunning())
    
    def testStartErrorHandling(self):
        
        q = MyQueue()
        q.addTask(waitOneSecond)
        q.addTask(raiseException)
        q.addTask(waitOneSecond)
        q.start()
        # nothing to assert
        # really only care that the raiseException process doesn't pitch an error
    
    def testStartMultipleProcesses(self):
        # test that we can run 3 seconds of tests with 2 procs in about 2 seconds.
        startTime = datetime.now()
        
        q = MyQueue(2)
        q.addTask(waitOneSecond)
        q.addTask(waitOneSecond)
        q.addTask(waitOneSecond)
        q.start()
        
        self.sleepCountAssert(startTime, q, 2)
    
    def testStartMultipleUse(self):
        q = MyQueue()
        q.addTask(waitOneSecond)
        q.start()
        
        while (q.isRunning()):
            time.sleep(.1)
        
        self.assertEqual(0, q.size())
        self.assertEqual(0, q.inFlight())
        self.assertFalse(q.isRunning())
        
        q.addTask(waitOneSecond)
        
        startTime = datetime.now()
        q.start()
        
        # it should take about 1 second to run the second task again
        self.sleepCountAssert(startTime, q, 1)
        
        
    def testStartMultipleStart(self):
        q = MyQueue()
        q.addTask(waitOneSecond)
        
        startTime = datetime.now()
        
        q.start()
        q.start()
        
        #should only take one second, aka the loaded task should not be run twice
        self.sleepCountAssert(startTime, q, 1)
        
    def testStartMoreProcsThanTasks(self):
        q = MyQueue(2)
        q.addTask(waitOneSecond)
        q.start()
        
        # this should not fail
        
    def sleepCountAssert(self, startTime, q, minSeconds):
        # utility function for time stamping
        while (q.isRunning()):
            time.sleep(.1)
        
        elapsedTime = datetime.now() - startTime
        
        self.assertTrue(elapsedTime.total_seconds() > minSeconds)
        self.assertTrue(elapsedTime.total_seconds() < minSeconds + 1)
            
    
def waitOneSecond():
    #print "waitOneSecond: Begin"
    time.sleep(1)
    #print "waitOneSecond: End"

def waitFiveSeconds():
    #print "waitFiveSeconds: Begin"
    time.sleep(5)
    #print "waitOneSecond: End"

def raiseException():
    #print "raiseException"
    raise Exception("Let the Queue Continue!")

 
def callbackFunc(theQueue):
    os.system("touch callback.txt")
    
if __name__ == '__main__':
    unittest.main()