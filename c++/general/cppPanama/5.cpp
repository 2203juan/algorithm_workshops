#include <bits/stdc++.h>
using namespace std;

int main(){
	double precio = 0.0;
	double descuento = 0.0;
	double costo = 0.0;

	cout<<"Ingrese el precio del articulo"<<endl;
	cin>>precio;
	if (precio >= 200){
		descuento = 0.15;
	}

	if (precio > 100 && precio < 200){
		descuento = 0.12;
	}

	if (precio < 100 ){
		descuento = 0.1;
	}

	costo = precio*(1-descuento);
	descuento *=100;
	cout<<"El costo es "<<costo<<" y se le aplico un descuento del "<<descuento<<"%"<<endl;



	return 0;
}