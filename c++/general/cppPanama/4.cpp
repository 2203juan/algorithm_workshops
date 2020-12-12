#include <bits/stdc++.h>
using namespace std;

int main(){
	int edad1 = 0;
	string nombre1 = "";

	int edad2 = 0;
	string nombre2 = "";

	int edad3 = 0;
	string nombre3 = "";

	cout<<"Ingrese el nombre de la persona1"<<endl;
	cin>>nombre1;

	cout<<"Ingrese la edad de la persona 1"<<endl;
	cin>>edad1;

	cout<<"Ingrese el nombre de la persona2"<<endl;
	cin>>nombre2;

	cout<<"Ingrese la edad de la persona 2"<<endl;
	cin>>edad2;

	cout<<"Ingrese el nombre de la persona3"<<endl;
	cin>>nombre3;

	cout<<"Ingrese la edad de la persona 3"<<endl;
	cin>>edad3;

	int mayor = edad1;
	string nombre_mayor = nombre1;
	if (edad2 > edad1){
		nombre_mayor = nombre2;
		mayor  = edad2;

		if (edad3 > edad2){
			nombre_mayor = edad3;
			mayor = edad3;
		}
	}

	if (edad3 > edad1 && edad3 > edad2){
		nombre_mayor = nombre3;
		mayor = edad3;
	}

	cout<<"El nombre del mayor es "<<nombre_mayor<<" con la edad = "<<mayor<<endl;
}