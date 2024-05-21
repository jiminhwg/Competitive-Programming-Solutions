#include <iostream>
using namespace std;
int main () {
    int NumberOfGames, A, D;
    string Results;

    cin >> NumberOfGames;
    cin >> Results;
    
    A = count(Results.begin(), Results.end(), "A");
    D = count(Results.begin(), Results.end(), "D");
    if (A > D) {
        cout << "Anton" << endl;
    }
}