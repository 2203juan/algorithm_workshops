# include <iostream>
using namespace std;

int main(){

	int tam = 10;

	float data1[tam];

	float data2[tam];

	float operados[tam];

	int i;

	cout<<"Ingrese los datos del arreglo 1:"<<endl;
	for (i = 0; i < tam; i++){
		cin>>data1[i];
	}

	cout<<"Ingrese los datos del arreglo 2:"<<endl;
	for (i = 0; i < tam; i++){
		cin>>data2[i];
	}

	int op = 0;

	cout<<"Seleccione la operacion que desea realizar con los arreglos:"<<endl;
	cout<<"1) Suma 2) Resta 3) Multiplicacion 4) Division"<<endl;

	cin>>op;

	if (op == 1){
		for(i = 0 ; i < tam; i++){operados[i] = data1[i] + data2[i];}
	}

	else if (op == 2){
		for(i = 0 ; i < tam; i++){operados[i] = data1[i] - data2[i];}
	}

	else if (op == 3){
		for(i = 0 ; i < tam; i++){operados[i] = data1[i] * data2[i];}
	}

	else if (op == 4){
		for(i = 0 ; i < tam; i++){
			if (data2[i] != 0)
				operados[i] = data1[i] * data2[i];
			else
				operados[i] =  -1;
		}
	}

	else {
		cout<<"Opcion no valida"<<endl;
	}

	cout<<"Vector resultado:"<<endl;
	for(i = 0 ; i < tam; i++){
		cout<<operados[i]<<"\t";
	}
	cout<<endl;

	return 0;
}
