# Count the number of prime numbers less than a non-negative number, n.

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        sieve = [1] * n
        sieve[0] = 0
        sieve[1] = 0
        
        for i in range(1, int(n ** 0.5) + 1):
            if sieve[i] == 1:
              for j in range(i*i, n, i):
                sieve[j] = 0
        
        return sum(sieve)

