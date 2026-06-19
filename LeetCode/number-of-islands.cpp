// https://leetcode.com/problems/number-of-islands/

#include <vector>

using namespace std;

class Solution {
private:
    int n,m;

    void mark(vector<vector<char>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] == '0') {
            return;
        }
        grid[i][j] = '0';

        mark(grid, i + 1, j);
        mark(grid, i - 1, j);
        mark(grid, i, j + 1);
        mark(grid, i, j - 1);
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        n = grid.size();
        m = grid[0].size();
        int rv = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    rv++;
                    mark(grid, i, j);
                }
            }
        }

        return rv;
    }
};
