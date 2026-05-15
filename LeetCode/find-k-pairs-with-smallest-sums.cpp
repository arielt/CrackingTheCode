// https://leetcode.com/problems/find-k-pairs-with-smallest-sums

#include <queue>
#include <set>

using namespace std;

class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        // min heap
        priority_queue<pair<int, pair<int,int>>, vector<pair<int, pair<int,int>>>, greater<pair<int, pair<int,int>>>> pq;
        set<pair<int,int>> used; // used indices
        vector<vector<int>> rv;  // return value

        if (nums1.empty() || nums2.empty()) {
            return rv;
        }

        pq.push({nums1[0] + nums2[0], {0,0}});

        while (!pq.empty()) {
            auto [sum, indices] = pq.top();
            auto [ind1, ind2] = indices;
            pq.pop();

            if (used.contains({ind1, ind2})) {
                continue;
            }

            rv.push_back({nums1[ind1], nums2[ind2]});                                    
            if (rv.size() == k) {
                return rv;
            }
            used.insert({ind1, ind2});

            if (ind1 + 1 < nums1.size()) {
                pq.push({nums1[ind1 + 1] + nums2[ind2], {ind1 + 1, ind2}});
            };

            if (ind2 + 1 < nums2.size()) {
                pq.push({nums1[ind1] + nums2[ind2 + 1], {ind1, ind2 + 1}});
            };
        }

        return rv;
    }
};
