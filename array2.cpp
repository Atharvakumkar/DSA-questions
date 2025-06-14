//Pass by reference

#include<iostream>
using namespace std;

void mod_arr(int arr[], int size){
    for(int i = 0; i < size; i++){
        arr[i] = arr[i] * 2;
    }
}

int main() {
    int arr[] = {2,4,6};

    mod_arr(arr, 3);

    for(int i=0;i<3;i++){
        cout << arr[i] << endl;
    }

    return 0;
}
