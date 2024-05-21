#include <iostream>
#include <cmath>
using namespace std;

int main () {
    int a, b;
    cin >> a >> b;
    int ans;
    ans = (pow(a, b)) - (pow(b, a));
    cout << ans;
    return 0;
}