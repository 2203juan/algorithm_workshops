#include <iostream>
using namespace std;

int positivos_en_impares(int arr[], int n){
    int ans = 0;
    for( int i = 0; i < n; i++){
        if (i%2 !=0 && arr[i] > 0){
            ans ++;
        }
    }

    return ans;
}

int main(){
    int n;
    cout<<"Ingrese el tamanio del vector: ";
    cin>> n;
    int arr[n];

    for ( int i = 0; i < n; i++){
        cout<<"Inrese el elemento "<<i<<" del vector: ";
        cin>>arr[i];
    }
    cout<<endl;

    int ans = 0;
    ans = positivos_en_impares(arr, n);
    cout<<"Hay "<<ans<<" numeros positivos en las posiciones impares del vector"<<endl;
}