// https://leetcode.com/problems/first-unique-character-in-a-string/

#include <string>

using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        int map[26] = {0};
        
        for (char c : s) {
            map[c - 'a']++;
        }

        for (int i = 0; i < s.size(); i++) {
            if (map[s[i] - 'a'] == 1) {
                return i;
            }
        }

        return -1;
    }
};
