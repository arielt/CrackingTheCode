// https://leetcode.com/problems/string-to-integer-atoi/description/

#include <string>

using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        if (s.empty()) {
            return 0;
        }

        int i = 0;
        int n = s.length();
        int sign = 1;
        long long rv = 0;

        // skip leading spaces
        while (i < n && s[i] == ' ') {
            i++;
        }

        if (i == n) {
            return 0;
        }

        // check the sign
        if (s[i] == '+') {
            i++;
        } else if (s[i] == '-') {
            sign = -1;
            i++;
        }

        // process digits
        while (i < n && isdigit(s[i])) {
            int d = s[i] - '0';
            rv = rv * 10 + d;

            if (sign == 1) {
                if (rv >= INT_MAX) {
                    return INT_MAX;
                }
            } else {
                if (sign * rv <= INT_MIN) {
                    return INT_MIN;
                }
            }

            i++;
        }   

        return rv * sign;
    }
};
