#ifndef __JUGADOR_H__
#define __JUGADOR_H__
#include <bits/stdc++.h>
using namespace std;

class Jugador{
	private:
		string nombre;
		int score = 0;
		int vidas = 3;
		int aciertos = 0;
	public:
		void setNombreJugador(string name){
			nombre = name;
		}

		void upScore(){
			score +=10;
		}

		void downLives(){
			vidas --;
		}

		int getScore(){
			return score;
		}

		int getLives(){
			return vidas;
		}

		void upAciertos(){
			aciertos++;
		}

		int getAciertos(){
			return aciertos;
		}

		string getNombre(){
			return nombre;
		}

		void reset(){
			score = 0;
			vidas = 3;
			aciertos = 0;	
		}

};
#endif