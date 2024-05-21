#include <iostream>
using namespace std;

int main () {
    int Red, Blue, NewRed, NewBlue;
    cin >> Red >> Blue;

    if (Red < Blue) {
        NewRed = Red - Red;
        NewBlue = Blue - Red;
        cout << Red << " " << NewBlue/2 << endl;
    }
    else {
        NewRed = Red - Blue;
        NewBlue = Blue - Blue;
        cout << Blue << " " << NewRed/2 << endl; 
    }
}   


    