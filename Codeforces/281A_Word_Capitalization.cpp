#include <iostream>
#include <string>

using namespace std;

int main () {
    string Word;
    cin >> Word;
    Word[0] = toupper(Word[0]);
    cout << Word << endl;
    return 0;
}


