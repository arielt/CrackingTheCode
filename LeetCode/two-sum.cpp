// https://leetcode.com/problems/two-sum/description/

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> map; // value --> index map

        for (int i = 0; i < nums.size(); i++) {
            int v = nums[i];
            if (map.contains(target - v)) {
                return {i, map[target - v]};
            }
            map[v] = i;
        }

        return {}; 
    }
};
