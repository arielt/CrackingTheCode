#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

// number of bits set to 1
int numberOfBits(unsigned long long int x) {
    int c = 0;
    while (x) {
        c++;
        x &= (x - 1); 
    }
    return c;
}

int main() {
    int n;
    unsigned long long int x;        
    cin >> n;    
    for (int i=0; i<n; i++) {
        cin >> x;
        if(numberOfBits(x-1) & 0x1)
            cout << "Louise" << endl;
        else
            cout << "Richard" << endl;
    }

    return 0;
}

