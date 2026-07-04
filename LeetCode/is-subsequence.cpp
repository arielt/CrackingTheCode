// https://leetcode.com/problems/is-subsequence/submissions/

#include <string>

using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0;
        int ls = s.size();

        if (!ls) {
            return true;
        }

        for (int j = 0; j < t.length(); j++) {
            if (t[j] == s[i]) {
                i++;
            }

            if (i == ls) {
                return true;
            }
        }

        return false;
    }
};
