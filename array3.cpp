//Linear Search Algorithm
#include<iostream>
using namespace std;

int LinearSearch(int arr[], int size, int target){
    for(int i=0; i < size; i++){
        if(arr[i] == target){
            return i;
        }
    }

    return -1;
}

int main() {
    int arr[] = {10,29,38,2,86,79};
    int target = 79;
    int size = 6;

    cout << LinearSearch(arr, size, target) << endl;    

    return 0;
}
