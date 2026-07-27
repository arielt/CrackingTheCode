// https://leetcode.com/problems/word-ladder/

#include <queue>
#include <unordered_set>
#include <string>

using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        unordered_set<string> visited;
        queue<string> q;
        q.push(beginWord);
        dict.erase(beginWord);
        int l = 1;

        while (!q.empty()) {
            int n = q.size();
            while (n) {
                string s = q.front();
                q.pop();
                if (s == endWord) {
                    return l;
                }
                // dict.erase(s);

                if (visited.contains(s)) {
                    continue;
                }
                visited.insert(s);

                for (int i = 0; i < s.size(); i++) {
                    char c = s[i];
                    for (int j = 0; j < 26; j++) {
                        s[i] = 'a' + j;
                        if (dict.contains(s)) {
                            q.push(s);
                            dict.erase(s);
                        }
                    }
                    s[i] = c;
                }

            n--;
            }
            l++;
        }

        return 0;
    }
};
