#ifndef __TABLERO_H__
#define __TABLERO_H__
#include <bits/stdc++.h>
using namespace std;

class Tablero{
	private:
		int size;
		int bombas = 0;
		vector< vector<string> > matriz_usuario;
		vector< vector<int> > matriz_interna;
	public:
		void startTablero(int size_,int bombas_){
			size = size_;
			bombas = bombas_;

			for(int i = 0;i < size; i++){
				vector<string> tmp;
				for( int j = 0;j < size;j++){
					tmp.push_back("#");
				}
				matriz_usuario.push_back(tmp);
			}

			vector< tuple<int,int> > posiciones_bombas;
			while (bombas > 0){
				tuple <int,int> tmp;
				srand (time(NULL)); 
				tmp = make_tuple(rand() % (size),rand() % (size));
				
				while (verificar(posiciones_bombas,tmp)==0){ //0 si no se puede usar 1 si si
					tmp = make_tuple(rand() % (size),rand() % (size));
				}

				posiciones_bombas.push_back(tmp); 
				bombas--;
			}

			for(int i = 0; i< size;i++){
				vector<int> tmp;
				for(int j = 0; j < size; j++){
					tmp.push_back(0);
				}

				matriz_interna.push_back(tmp);
			}

			int fila,columna;
			for(int i = 0; i< posiciones_bombas.size();i++){
				fila = get<0>(posiciones_bombas[i]);
				columna = get<1>(posiciones_bombas[i]);

				matriz_interna[fila][columna] = 1;
			}



		}

		int verificar(vector<tuple<int,int>> posiciones_bombas,tuple<int,int> tmp){
			int fila = get<0>(tmp);
			int columna = get<1>(tmp);
			int a,b;
			for(int i = 0;i < posiciones_bombas.size();i++){
				a = get<0>(posiciones_bombas[i]);
				b = get<1>(posiciones_bombas[i]);

				if (fila==a && columna==b){
					return 0;
				}
			}

			return 1;
		}

		vector< vector<string> > getMatrizUsuario(){
			return matriz_usuario;
		}

		vector< vector<int> > getMatrizInterna(){
			return matriz_interna;
		}

		int unlockBlock(int fila, int columna){
			int ans;//1 si no hay bomba 0 de lo contrario
			if (matriz_interna[fila][columna]!=1){
				matriz_usuario[fila][columna] = ":)";
				ans = 1;
			}

			else{
				matriz_usuario[fila][columna] = "X";
				ans = 0;
			}

			return ans;

		}

		void show(){
			for( int i = 0; i < size;i++){
				for(int j = 0; j< size;j++){
					cout<<matriz_usuario[i][j]<<"\t";
				}
				cout<<endl;
			}
			cout<<endl;
		}

		void showInterna(){
			for( int i = 0; i < size;i++){
				for(int j = 0; j< size;j++){
					cout<<matriz_interna[i][j]<<"\t";
				}
				cout<<endl;
			}
			cout<<endl;
		}

		int getSize(){
			return size;
		}

		void reset(){
			matriz_usuario.clear();
			matriz_interna.clear();
		}

		int isOpen(int fila,int col){
			if (matriz_usuario[fila][col]=="#"){
				return 1;
			}

			return 0;

		}


};


#endif