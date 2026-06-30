// https://leetcode.com/problems/powx-n/

#include <cstdlib>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        double rv = 1;
        long p = labs(n);

        while (p) {
            if (p & 1) {
                rv *= x;
            }

            x *= x;
            p >>= 1;
        }

        return (n > 0) ? rv : (1 / rv);        
    }
};
