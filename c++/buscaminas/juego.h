#ifndef __JUEGO_H__
#define __JUEGO_H__
#include <bits/stdc++.h>
using namespace std;

class Juego {
	private:
		Jugador j1;
		Tablero t1;
		int cant_bombas = 0;

	public: 
		void start(){
			cout<<"---Bienvenido a Buscaminas---"<<endl;
			
			string nombre;
			cout<<"¿Cual es tu nombre?"<<endl;
			cin>>nombre;
			
			j1.setNombreJugador(nombre);
			cout<<"Genial "<<nombre<<", vamos a comenzar!!"<<endl;
			menu();

		}

		void menu(){
			cout<<"***Selecciona un Nivel***"<<endl;
			cout<<"1) Bajo"<<endl;
			cout<<"2) Medio"<<endl;
			cout<<"3) Alto"<<endl;
			cout<<"0) Salir del juego"<<endl;
			int nivel;

			cin>>nivel;

			while(nivel!=0){
				if (nivel==1){
					t1.startTablero(3,4);
					cant_bombas = 4;
				}

				else if (nivel==2){
					t1.startTablero(4,6);
					cant_bombas = 6;
				}

				else{
					t1.startTablero(5,10);
					cant_bombas = 10;
				}

				jugar();
				t1.reset();
				cout<<"***Selecciona un Nivel***"<<endl;
				cout<<"1) Bajo"<<endl;
				cout<<"2) Medio"<<endl;
				cout<<"3) Alto"<<endl;
				cout<<"0) Salir del juego"<<endl;
				cin>>nivel;


			}


		}

		void jugar(){
			t1.show();
			//t1.showInterna(); solo para saber donde estan las bombas
			int size = t1.getSize();
			cout<<"Ahora debes seleccionar una posicion para destapar"<<endl;
			
			cout<<"Selecciona una fila (entre 0 y "<<size-1<<" )"<<endl;
			int fila;
			cin>>fila;

			int aciertos = 0;
			int fullsize = t1.getSize()*t1.getSize();
			while (j1.getLives() > 0 && (aciertos < (fullsize-cant_bombas))){
				while (fila < 0 || fila > size-1){
					t1.show();
					cout<<"Por favor ingresa una fila valida (entre 0 y "<<size-1<<" )"<<endl;
					cin>>fila;
				}

				cout<<"Selecciona una columna (entre 0 y "<<size-1<<" )"<<endl;
				int columna;
				cin>>columna;

				while (columna < 0 || columna > size-1){
					t1.show();
					cout<<"Por favor ingresa una columna valida (entre 0 y "<<size-1<<" )"<<endl;
					cin>>columna;
				}
				int libre = t1.isOpen(fila,columna);

				if (libre){
					int bomba = t1.unlockBlock(fila,columna);
					t1.show();

					if (bomba==0){
						cout<<"Ups-- hay una bomba!!!!!!"<<endl;
						j1.downLives();
					}

					else{
						cout<<"Genial!! - No hay bomba!! "<<endl;
						j1.upAciertos();
						j1.upScore();
					}

					cout<<"Tienes "<<j1.getScore()<<" puntos y "<<j1.getLives()<<" vidas"<<endl;
					aciertos = j1.getAciertos();
				}

				if (libre==0){
					cout<<"Esa ya la elegiste, selecciona otra "<<endl;
				}

				if(j1.getLives() > 0 && aciertos < (fullsize-cant_bombas)){
					cout<<"Selecciona una fila (entre 0 y "<<size-1<<" )"<<endl;
					cin>>fila;
				}
				
			}

			if (j1.getLives() > 0 && (j1.getAciertos()== (t1.getSize()*t1.getSize())-cant_bombas)){
				cout<<"Felicitaciones "<<j1.getNombre()<<", Ganaste!!"<<endl;
			}

			else{
				cout<<"Game Over..."<<endl;
			}

			t1.reset();
			j1.reset();


		}

};


#endif