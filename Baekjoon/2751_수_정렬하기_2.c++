#include <iostream>
#include <list>
using namespace std;

int main() {
    int n, numbers;
    cin >> n;
    list<int> List;
    for (int i = 0; i < n; i++) { //for a in range(0,n)
        cin >> numbers;
        List.push_back (numbers); //List.append(numbers)
    }
    List.sort();
    for (int item : List) { //for item in List 
        cout << item << endl; 
    }
}