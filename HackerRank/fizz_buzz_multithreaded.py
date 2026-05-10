# Write a program that outputs the string representation of numbers from 1 # to n, however:

# If the number is divisible by 3, output "fizz".
# If the number is divisible by 5, output "buzz".
# If the number is divisible by both 3 and 5, output "fizzbuzz".
# For example, for n = 15, we output: 1, 2, fizz, 4, buzz, fizz, 7, 8,
# fizz, buzz, 11, fizz, 13, 14, fizzbuzz.
    
from threading import Lock

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.lock_fizz = Lock()
        self.lock_buzz = Lock()
        self.lock_fizz_buzz = Lock()
        self.lock_number = Lock()
        
        self.lock_fizz.acquire()
        self.lock_buzz.acquire()
        self.lock_fizz_buzz.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in xrange(3, self.n + 1, 3):
            if i%5 == 0:
                continue
            self.lock_fizz.acquire()
            printFizz()
            self.lock_number.release()    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in xrange(5, self.n + 1, 5):
            if i%3 == 0:
                continue
            self.lock_buzz.acquire()
            printBuzz()
            self.lock_number.release()    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in xrange(15, self.n + 1, 15):
            self.lock_fizz_buzz.acquire()
            printFizzBuzz()
            self.lock_number.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in xrange(1, self.n + 1):
            self.lock_number.acquire()
            if i%3 == 0 and i%5 == 0:
                self.lock_fizz_buzz.release()
            elif i%3 == 0:
                self.lock_fizz.release()
            elif i%5 == 0:
                self.lock_buzz.release()
            else:
                # print i
                printNumber(i)
                self.lock_number.release()

