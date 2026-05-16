// https://leetcode.com/problems/intersection-of-two-arrays

#include <set>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s;
        vector<int> rv;

        vector<int>& n1 = (nums1.size() < nums2.size()) ? nums1 : nums2;
        vector<int>& n2 = (nums1.size() < nums2.size()) ? nums2 : nums1;

        for (int n : n1) {
            s.insert(n);
        };

        for (int n : n2) {
            if (s.contains(n)) {
                rv.push_back(n);
                s.erase(n);
            }
        }

        return rv;
    }
};
