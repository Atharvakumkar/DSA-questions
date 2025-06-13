//To find the smallest value in array

#include<iostream>
using namespace std;

int main() {
    int marks[] = {100,89,98,76,91};
    int size = 5;
    int small = INT_MAX;

   for(int i=0; i<size; i++ ) {
    if(marks[i]<small) {
        small = marks[i];
    }
   }

   cout << small;

    return 0; 

}
