#include <iostream>
using namespace std;

int main () {
    long long int Number;
    cin >> Number;
    if (Number % 2 == 0) {
        cout << Number/2 <<endl;
    }
    else {
        cout << ((Number/2 +1)*(-1)) << endl;
    }
}