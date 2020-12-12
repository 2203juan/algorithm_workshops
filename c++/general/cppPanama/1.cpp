#include <bits/stdc++.h>
using namespace std;

double get_sueldo(double horas_trabajadas, double valor_hora){

	double saldo = 0;

	if (horas_trabajadas > 40){
		saldo += (40*valor_hora);
		horas_trabajadas -= 40;

		saldo += (horas_trabajadas*(2.0*valor_hora));

	}

	else {
		saldo += horas_trabajadas*valor_hora;
	}


	return saldo;



}
int main(){
	double horas_trabajadas = 0.0;
	double valor_hora = 0.0;

	cout<<"Ingrese las horas trabajadas en la semana"<<endl;
	cin>>horas_trabajadas;

	cout<<"Ingrese el valor pagado por hora"<<endl;
	cin>>valor_hora;

	double sueldo = get_sueldo(horas_trabajadas, valor_hora);

	cout<<"El sueldo semanal es: "<<sueldo<<endl;

	return 0;
}