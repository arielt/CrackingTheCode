// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

#include <vector>

using namespace std;

// search for cliff
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0;
        int r = nums.size() - 1;

        while (l < r) {
            int m = (l + r) / 2;
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        return nums[l];
    }
};
