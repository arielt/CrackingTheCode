// https://leetcode.com/problems/unique-email-addresses/

#include <unordered_set>

using namespace std;

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> set;
        
        for (auto& email : emails) {
            string unique;

            for (char c : email) {
                if (c == '+' || c == '@') {
                    break;
                }

                if (c == '.') {
                    continue;
                }

                unique += c;
            }

            unique += email.substr(email.find('@'));
            set.insert(unique);
        }        

        return set.size();
    }
};
