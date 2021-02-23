# include <iostream>

using namespace std;

int main(){

	// Matriz 1 - matriz estática

	int n = 7;
	int m = 4;
	int i,j;
	
	float matriz[n][m] = {{1.0,2.0,3.0,4.0},
						  {1.0,2.0,3.0,4.0},
						  {1.0,2.0,3.0,4.0},
						  {1.0,2.0,3.0,4.0},
						  {1.0,2.0,3.0,4.0},
						  {1.0,2.0,3.0,4.0},
						  {1.0,2.0,3.0,4.0}};
	
	cout<<"Matriz 1\n"<<endl;
	for( i = 0; i < n; i++){
		for (j = 0; j < m; j++){
			cout<<matriz[i][j]<<"\t";
		}
		cout<<endl;
	}

	// Matriz 2 - matriz dinámica
	float **a = (float **)malloc(n * sizeof(float*));
	for(int i = 0; i < n; i++)
		a[i] = (float *)malloc(m * sizeof(float));

	cout<<"Ingrese los valores de la matriz 2"<<endl;
	for (i = 0; i < n; i++){
		for(j = 0; j < m; j++){
			cout<<"Ingrese el dato de la casilla ("<<i<<","<<j<<") : ";
			cin>>a[i][j];
		}
	}

	cout<<"Matriz 2\n"<<endl;
	for( i = 0; i < n; i++){
		for (j = 0; j < m; j++){
			cout<<a[i][j]<<"\t";
		}
		cout<<endl;
	}

	return 0;
}