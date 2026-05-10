#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

/*
 * https://www.hackerrank.com/challenges/sparse-arrays
 */

int main() {
    int n;
    string s;
    map<string,int> myMap;

    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> s;
        map<string, int>::iterator it = myMap.find(s);
        if (it == myMap.end()) {
            // not found
            myMap.insert(pair<string,int> (s,1));
        } else {
            // found
            it->second = (it->second + 1);
        }
    }

    cin >> n;
    for (int i=0; i < n; i++) {
        cin >> s;
        map<string, int>::iterator it = myMap.find(s);
        if (it == myMap.end()) {
            cout << 0 << endl;
        } else {
            cout << it->second << endl;
        }
    }
    return 0;
}
