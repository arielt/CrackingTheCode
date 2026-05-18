// https://leetcode.com/problems/group-anagrams/

#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        vector<vector<string>> rv; // return value

        // build the map
        for (auto& s: strs) {
            string key = s;
            sort(key.begin(), key.end());
            map[key].push_back(s);
        }

        // construct return value
        for (auto& pair: map) {
            rv.push_back(pair.second);
        }

        return rv;
    }
};
