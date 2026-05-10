// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

class Solution {
public:
    int minAddToMakeValid(string s) {
        int open = 0; // 
        int missing = 0; // openers to add
        
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
