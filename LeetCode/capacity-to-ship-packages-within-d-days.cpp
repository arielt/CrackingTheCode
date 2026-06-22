// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

#include <numeric>
#include <vector>

using namespace std;

// binary search for ship capacity
class Solution {
private:
    bool ships(int cap, vector<int>& weights, int days) {
        int curr = 0;

        for (int w: weights) {
            curr += w;
            if (curr > cap) {
                days--;
                if (days <= 0) {
                    return false;
                }
                curr = w;
            }
        }

        return true;
    }

public:
    int shipWithinDays(vector<int>& weights, int days) {
        int l = *max_element(weights.begin(), weights.end());
        int r = accumulate(weights.begin(), weights.end(), 0);
        int m;
        int rv = r;

        while (l <= r) {
            m = (l + r) / 2;

            if (ships(m, weights, days)) {
                rv = min(m, rv);
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return rv;
    }
};
