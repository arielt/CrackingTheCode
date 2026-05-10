# The same instance of FooBar will be passed to two different threads.
# Thread A will call foo() while thread B will call bar().
# Modify the given program to output "foobar" n times.

from threading import Lock

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.l1 = Lock()
        self.l2 = Lock()
        self.l2.acquire()


    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.l1.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.l2.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.l2.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.l1.release()

