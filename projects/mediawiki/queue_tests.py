import unittest
from queue import Queue
import time

class QueueTests(unittest.TestCase):

    def testConstructor(self):
        q = Queue(1)
        self.assertEqual(1, q._parallelism)
        
        self.assertRaises(Exception, Queue, 0)
        self.assertEqual(0, q.size())
        self.assertFalse(q.isRunning())
        self.assertEqual(0, q.inFlight())
        
        q.addTask(self.waitOneSecond)
        self.assertEqual(1, q.size())
        
    def testSize(self):
        q = Queue(1)
        self.assertEqual(0, q.size())
        
    def waitOneSecond(self):
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()