# https://leetcode.com/problems/print-in-order/

from threading import Lock

class Foo(object):
    def __init__(self):
        self.first_lock = Lock()
        self.second_lock = Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_lock.release()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """

        self.first_lock.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.first_lock.release()
        self.second_lock.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        self.second_lock.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.second_lock.release()

