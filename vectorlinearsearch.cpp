//Linear search on vector
#include <iostream>
#include <vector>
using namespace std;

int LinearSearch(vector<int> vec, int target) {
    for (int value : vec) {
        if (value == target) {
            return value;
        }
    }
    return -1;
}

int main() {
    vector<int> vec = {10, 12, 34, 24};
    int target = 34;

    int result = LinearSearch(vec, target);
    
    if (result != -1) {
        cout << "Value found: " << result << endl;
    } else {
        cout << "Value not found" << endl;
    }

    return 0;
}
