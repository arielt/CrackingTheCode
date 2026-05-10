// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

class Solution {
public:
    int minAddToMakeValid(string s) {
        int open = 0; // number of open parentheses
        int missing = 0; // number of open parentheses to add
        
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
