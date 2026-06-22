// https://leetcode.com/problems/search-insert-position/submissions/2033356797/

#include <vector>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) {
            int m = (l + r) / 2;

            if (nums[m] == target) {
                return m;
            }

            if (nums[m] >  target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return l;
    }
};
