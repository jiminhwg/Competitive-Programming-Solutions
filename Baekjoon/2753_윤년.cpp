#include <iostream>
using namespace std;

int main () {
    int Year;
    cin >> Year;
    if (Year%4 == 0) {
        if (Year%100 != 0) {
            cout << 1 << endl;
        }
        else if (Year%100 == 0) {
            if (Year%400 == 0) {
                cout << 1 << endl;
            }
            else {
                cout << 0 << endl;
            }
        }
    }
    else if (Year%4 != 0)  {
        cout << 0 << endl;
    }
    else {
        cout << 0 << endl;
    }
}