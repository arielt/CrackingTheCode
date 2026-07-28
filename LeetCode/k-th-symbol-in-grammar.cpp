// https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution {
public:
    int kthGrammar(int n, int k) {
        // recursion ... if n == 1, return 0
        // query (n - 1, (k + 1) / 2), return 0,1 taking into account k parity
        
        if (n == 1) {
            return 0;
        }

        int p = kthGrammar(n - 1, (k + 1) / 2);

        if (k % 2) { // 1-indexed
            return p;
        } else {
            return !p;
        }
    }
};
