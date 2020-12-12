#include <bits/stdc++.h>
using namespace std;

double get_costo(int horas){
	double costo = 0.0;


	if (horas > 2){
		costo += (2.0*5.0);
		horas -=2;


		if (horas > 3){
			costo +=(3.0*4.0);
			horas -=3;


			if (horas > 5){
				costo +=(5.0*3.0);
				horas -= 5;

				if (horas > 1){
					costo += (horas*2.0);
				}
			}

			else{
				costo += (horas*3.0);
				horas -= 5;
			}
		}

		else {
			costo += (horas*4.0);
			horas -=3;
		}



	}

	else {
		costo += (horas*5.0);
		horas -=2;
	}



 	return costo;
	


}

int main(){
	int horas = 0;
	double costo = 0.0;
	cout<<"Ingrese la cantidad de horas que estuvo en el parqueadero"<<endl;
	cin>>horas;

	horas = get_costo(horas);

	cout<<"Pague "<<horas<<endl;

	return 0;
}