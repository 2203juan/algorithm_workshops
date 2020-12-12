#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#define max(a, b) a >= b ? a : b
using namespace std;


vector<string> leer(char *name){
	string line;
	vector<string> lineas;

	ifstream myfile (name);

	if (myfile.is_open()){
		
		while ( getline (myfile,line) ){
		  lineas.push_back(line);
		}

	myfile.close();
	}

	return lineas;
}


int size_larger_string(vector<string> vec){
	int max_val = 0;

	for (int i = 0; i < vec.size(); i++){
		max_val = max(max_val,vec[i].size());
	}

	return max_val;
}

vector<string> crear_tablero(int filas, int columnas){
	vector<string> tablero;
	string tmp = "";

	for (int j = 0; j < columnas; j++){ tmp +="x";}
	for (int i = 0; i < filas; i++  ){
		tablero.push_back(tmp);
	}

	return tablero;

}

void imprimir_tablero(vector<string> vec){

	for(int i = 0; i < vec.size(); i++){
		cout<<vec[i]<<endl;
	}

}

void descubir_palabra(int fila, vector<string> &tablero, vector<string> deportes){
	int j = 0;

	while (j < deportes[fila].size()){
		tablero[fila][j] = deportes[fila][j];
		j+=1;
	}

}

int main(){
	vector<string> deportes = leer("deportes.txt");
	vector<string> descripciones  = leer("descripcion.txt");
	int max_size = size_larger_string(deportes);

	vector<string> tablero = crear_tablero(deportes.size(), max_size);

	vector<bool> visited(deportes.size(), false);
	cout<<"Bienvenido a AdivinaSports!!"<<endl;
	cout<<endl;
	int band = deportes.size();
	while (band !=0){
		cout<<"Tablero de palabras"<<endl;
		imprimir_tablero(tablero);
		cout<<endl;
		for (int i = 0; i< deportes.size(); i++){
			if (!visited[i])
				cout<<i<<". "<<descripciones[i]<<endl;
			cout<<endl;
		}

		int a_adivinar = 0;

		cout<<"Ingrese el numero de la descripcion que quiere adivinar: ";
		cin>>a_adivinar;

		while (a_adivinar < 0 || a_adivinar > deportes.size() || visited[a_adivinar]){
			cout<<"Numero invalido, ingresa un numero de los mostrados en las descripciones"<<endl;
			cout<<"Ingrese el numero de la descripcion que quiere adivinar: ";
			cin>>a_adivinar;
		}

		string palabra_a_adivinar;
		cout<<"Ingresa el nombre del deporte correspondiente a la descripcion que seleccionaste: ";
		cin>> palabra_a_adivinar;

		if (palabra_a_adivinar == deportes[a_adivinar]){
			cout<<"Muy bien, adivinaste la palabra!!"<<endl;
			visited[a_adivinar] = true;
			band--;
			descubir_palabra(a_adivinar, tablero, deportes);

		}

		else{
			cout<<"UPS!!, sigue intentando"<<endl;
		}

		

	}

	return 0;
}
