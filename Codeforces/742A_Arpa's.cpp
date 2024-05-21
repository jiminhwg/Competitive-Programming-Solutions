#include <iostream>
using namespace std;

int main () {
    int Exponent, Number;
    cin >> Exponent;

    Number = pow(1378, Exponent);
    cout << Number%10 << endl;

}
