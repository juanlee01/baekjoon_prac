#include <iostream>

using namespace std;
int main(){
    int n=0;
    cin >> n;
    int* arr = new int[n];

    for(int i =0; i<n; i++){
        cin >> arr[i];
    }

    int  v=0;
    cin >> v;
    int count = 0;
    for(int i =0; i<n; i++){
        if(arr[i] == v){
            count++;
        }
    }
    cout << count;

    delete[] arr;
}