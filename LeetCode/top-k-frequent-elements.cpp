// https://leetcode.com/problems/top-k-frequent-elements/

#include <queue>
#include <ranges>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq; // frequency counter
        vector<int> rv;

        // count elements: O(N) / O(N)
        for (int n : nums) {
            freq[n]++;
        }

        // using min heap: O(N) + O(MLog(K)) / O(N) + O(K)
        // M - number of unique elements
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        for (auto& [num, count] : freq) {
            pq.push({count, num});
            if (pq.size() > k) {
                pq.pop();
            }
        }

        while(!pq.empty()) {
            rv.push_back(pq.top().second);
            pq.pop();
        }

        return rv;
        // // distribute to buckets: O(N) / O(N)
        // vector<vector<int>> buckets(nums.size() + 1);   // buckets
        // for (auto& [num, count] : freq) {
        //     buckets[count].push_back(num);
        // }

        // // construct response: O(N) / O(N)
        // for (auto& vec : buckets | views::reverse) {
        //     for (int n : vec) {
        //         if (rv.size() == k) {
        //             return rv;
        //         }
        //         rv.push_back(n);
        //     }
        // }      
        //
        // return rv;
    }
};
