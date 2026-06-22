// https://leetcode.com/problems/longest-substring-without-repeating-characters/

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        int l = 0;
        int rv = 0;

        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            if (map.contains(c) && map[c] >= l) {
                l = map[c] + 1;
            }

            map[c] = i;
            rv = max(rv, i - l + 1);
        }

        return rv;
    }
};
