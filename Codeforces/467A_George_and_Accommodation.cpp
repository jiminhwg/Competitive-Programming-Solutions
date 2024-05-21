#include <iostream>
using namespace std;

int main () {
    int Number, Rooms, People, count;
    cin >> Number;
    count = 0;
    for(int i = 0; i < Number; i++) {
        cin >> Rooms >> People;
        if (Rooms + 1 < People) {
            count += 1;
        }
    }
    cout << count << endl;
    return 0;
}