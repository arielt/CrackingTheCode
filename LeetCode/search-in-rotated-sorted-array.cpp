// https://leetcode.com/problems/search-in-rotated-sorted-array/

#include <vector>

using namespace std;

// Binary search, while checking if the chunk is sorted.
// Go to the other side otherwise.

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        int m;

        while (l <= r) {
            m = (l + r) / 2;
            if (target == nums[m]) {
                return m;
            }

            if (nums[m] >= nums[l]) {
                // left is sorted
                if (target >= nums[l] && target < nums[m]) {
                    // the target is in the left part
                    r = m - 1;
                } else {
                    // search in the right part
                    l = m + 1;
                }
            } else {
                // right is sorted
                if (target > nums[m] && target <= nums[l]) {
                    // the target is in the right part
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }

        return -1;
    }
};
