#include <iostream>
#include <string>
using namespace std;

int main () {
    string First, Second;
    cin >> First >> Second;
    
    for(char i = 0; i < First.length(); i++) {
        First[i] = tolower(First[i]);
    }
    
    for(char i = 0; i < Second.length(); i++) {
        Second[i] = tolower(Second[i]);
    }

    if (First == Second) {
        cout << 0 << endl;
    }
    else if (First < Second) {
        cout << -1 << endl;
    }
    else {
        cout << 1 << endl;
    }
    return 0;
}