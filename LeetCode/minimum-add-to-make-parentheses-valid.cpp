// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

#include <iostream>
using namespace std;

class Solution {
public:
    int minAddToMakeValid(string s) {
        int open = 0; // number of open brackets not closed yet
        int missing = 0; // number of open brackets to add

        for(char c : s) {
            if (c == '(') {
                open++;
            } else {
                if (!open) {
                    missing++;
                } else {
                    open--;
                }
            }
        }

        return open + missing;
    }
};
