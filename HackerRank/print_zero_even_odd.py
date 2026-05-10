# Each of the threads is given a printNumber method to output an integer. # Modify the given program to output the series 010203040506... where the # length of the series must be 2n.

from threading import Lock

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.l_zero = Lock()
        self.l_even = Lock()
        self.l_odd = Lock()
        
        self.l_even.acquire()
        self.l_odd.acquire()
                        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        if self.n == 0:
            return

        for i in range(0, self.n):
            self.l_zero.acquire()
            printNumber(0)
            if i%2 == 0:
                self.l_odd.release()
            else:
                self.l_even.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        num = 2
        while num <= self.n:
            self.l_even.acquire()
            printNumber(num)
            self.l_zero.release()
            num += 2
        
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        num = 1
        while num <= self.n:
            self.l_odd.acquire()
            printNumber(num)
            self.l_zero.release()
            num += 2
