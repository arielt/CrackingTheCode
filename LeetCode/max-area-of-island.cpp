// https://leetcode.com/problems/max-area-of-island/description/

#include <vector>

using namespace std;

class Solution {
private:
    int n,m;
    int rec(vector<vector<int>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i == n || j == m || grid[i][j] != 1) {
            return 0;
        }
        grid[i][j] = -1;
        return 1 + rec(grid, i + 1, j) + rec(grid, i - 1, j) + rec(grid, i, j + 1) + rec(grid, i, j - 1);
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        int rv = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    rv = max(rv, rec(grid, i, j));
                }
            }
        }

        return rv;
    }
};
