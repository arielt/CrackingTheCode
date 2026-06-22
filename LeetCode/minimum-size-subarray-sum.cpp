// https://leetcode.com/problems/minimum-size-subarray-sum/description/

#include <vector>

using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        // no need in help array, calculate running sum
        // every step try to shrink it from the left
        int l = 0;
        int size = nums.size();
        int rv = size + 1;
        int curr = 0;
        int notFound = rv;

        for (int i = 0; i < size; i++) {
            curr += nums[i];
            while (curr >= target && l <= i) {
                rv = min(rv, i - l + 1);
                curr -= nums[l];
                l++;
            }
        }

        if (rv == notFound) {
            return 0;
        }

        return rv;
    }
};
