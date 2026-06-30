// https://leetcode.com/problems/move-zeroes/

#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int z = 0; // index of zeroes
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i]) {
                swap(nums[z], nums[i]);
                z++;
            }
        }
    }
};
