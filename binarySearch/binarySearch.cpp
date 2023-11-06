#include <iostream>
using namespace std;

int binarySearch(int arr[],int start, int end, int item){
    int mid;
    while (start <= end){
        mid = (start + end) / 2;
        if (arr[mid] == item){
            return mid;
        }else if (arr[mid] > item){
            end = mid - 1;
        }else if (arr[mid] < item){
            start = mid + 1;
        }
    }
    return -1;
}

int main(){
    int array[] = {2,5,6,9,18};
    int x = 6;
    int n = sizeof(array) / sizeof(array[0]);
    int result = binarySearch(array,0,n - 1, x);
    cout << result;
    
    return 0;
}
