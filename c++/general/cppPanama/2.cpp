#include <bits/stdc++.h>
using namespace std;


string get_regalo(double presupuesto){

	string regalo = "";
	if (presupuesto <= 10.0){
		regalo = "Tarjeta";
	}

	if (presupuesto >= 11 && presupuesto <= 100){
		regalo = "Chocolates";
	}

	if (presupuesto >=101 && presupuesto<= 250){
		regalo = "Flores";
	}

	if (presupuesto >= 251){
		regalo = "Anillo";
	}

	return regalo;

}

int main(){
	cout<<"Te vamos a ayudar a escoger el regalo para tu ser querido"<<endl;
	double presupuesto = 0.0;

	cout<<"Ingrese su presupuesto"<<endl;
	cin>>presupuesto;

	string regalo = get_regalo(presupuesto);

	cout<<"Le recomendamos regalarle "<<regalo<<endl;

	return 0;
}