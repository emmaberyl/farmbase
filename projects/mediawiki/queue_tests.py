import unittest
from queue import Queue
import time

class QueueTests(unittest.TestCase):

    def testConstructor(self):
        q = Queue()
        self.assertEqual(1, q._parallelism)
        
        self.assertRaises(Exception, Queue, 0)
        self.assertEqual(0, q.size())
        self.assertFalse(q.isRunning())
        self.assertEqual(0, q.inFlight())
        
    def testSize(self):
        
        q = Queue(1)        
        self.assertEqual(0, q.size())
        
        q.addTask(self.waitOneSecond)
        self.assertEqual(1, q.size())
    
    def testStart(self):
        q = Queue()
        
        q.addTask(self.waitOneSecond)
        q.addTask(self.waitFiveSeconds)
        q.addTask(self.waitOneSecond)
        self.assertEqual(3, q.size())
        self.assertFalse(q.isRunning())
        self.assertEqual(0, q.inFlight())
        print q._parallelism
        
        q.start()
        time.sleep(1)
        #print q._jobs
        #self.assertEqual(1, q.inFlight())
        #self.assertEqual(2, q.size())
        self.assertTrue(q.isRunning())
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
    
    # def testStartErrorHandling(self):
        # q = Queue()
        
        # q.addTask(self.waitOneSecond)
        # q.addTask(self.raiseException)
        # q.addTask(self.waitFiveSeconds)
        # q.addTask(self.waitOneSecond)
        
        # q.start()
    
    
    def waitOneSecond(self):
        print "waitOneSecond: Begin"
        time.sleep(1)
        print "waitOneSecond: End"
    
    def waitFiveSeconds(self):
        print "waitFiveSeconds: Begin"
        time.sleep(5)
        print "waitOneSecond: End"
    
    def raiseException(self):
        print "raiseException"
        raise Exception("Let the Queue Continue!")

if __name__ == '__main__':
    unittest.main()