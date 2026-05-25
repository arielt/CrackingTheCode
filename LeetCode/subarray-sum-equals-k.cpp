// https://leetcode.com/problems/subarray-sum-equals-k/

#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> prefix_sum;
        prefix_sum[0] = 1;
        int curr = 0;
        int rv = 0;

        for (int n : nums) {
            curr += n;
            if (prefix_sum.contains(curr - k)) {
                rv += prefix_sum[curr - k];
            }
            prefix_sum[curr]++;
        }

        return rv;
    }
};