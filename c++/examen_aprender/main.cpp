#include <iostream>
#include <stdlib.h>
#include <windows.h>
using namespace std;

int totalpuntos = 0;
void pausa(){
    for(int m=1;m<=5;m++){
        cout<<".";
        Sleep(2000);
        }
    cout<<endl;
}

double obtener_porc(int buenas){
    return (buenas/3.0)*100;
}

void examen_vertebrados(){
    pausa();
    int ans = 0;
    int buenas = 0;

    cout<<"¿son las ballenas, las víboras y los gatos parte de la especie de vertebrados?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==1)
        buenas++;

    cout<<"¿son los vertebrados originarios del agua salada?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==2)
        buenas++;

    cout<<"¿Tienen los vertebrados una columna vertebral?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==1)
        buenas++;
    
    double porc = obtener_porc(buenas);
    cout<<"Obtuviste "<<porc<<"% de las preguntas correctas"<<endl;
    
}

void examen_moluscos(){
    pausa();
    int ans = 0;
    int buenas = 0;

    cout<<"¿Hay 36.000 especies de moluscos extintos?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==2)
        buenas++;

    cout<<"¿Son los moluscos invertebrados?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==1)
        buenas++;

    cout<<"¿Las almejas, ostras y gaviotas hacen parte de la especie de moluscos?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==2)
        buenas++;
    
    double porc = obtener_porc(buenas);
    cout<<"Obtuviste "<<porc<<"% de las preguntas correctas"<<endl;
}

void examen_anelidos(){
    pausa();
    int ans = 0;
    int buenas = 0;

    cout<<"¿Pueden los anélidos sobrevivir en clima secos?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==2)
        buenas++;

    cout<<"¿Es una cucaracha  un anélido?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==2)
        buenas++;

    cout<<"¿Pueden sobrevivir los anélidos sin agua?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==1)
        buenas++;
    
    double porc = obtener_porc(buenas);
    cout<<"Obtuviste "<<porc<<"% de las preguntas correctas"<<endl;
}

void examen_nematodos(){
    pausa();
    int ans = 0;
    int buenas = 0;

    cout<<"¿Son los nematodos parecidos a los anélidos?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==2)
        buenas++;

    cout<<"¿Los nematodos se alimentan de carne?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==2)
        buenas++;
    
    cout<<"¿los cuerpos de los nematodos son duros y rígidos?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==2)
        buenas++;

    double porc = obtener_porc(buenas);
    cout<<"Obtuviste "<<porc<<"% de las preguntas correctas"<<endl;
}

void examen_antropodos(){
    pausa();
    int ans = 0;
    int buenas = 0;

    cout<<"¿Los artrópodos tienen esqueleto?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==2)
        buenas++;

    cout<<"¿Es un cangrejo un artrópodo?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==1)
        buenas++;

    cout<<"¿Los artrópodos tienen el cuerpo segmentado?"<<endl;
    cout<<"1) Verdadero\n2) Falso"<<endl;
    cout<<"Ingresa tu respuesta"<<endl;
    cin>>ans;
    cout<<endl;

    if (ans==1)
        buenas++;
    
    double porc = obtener_porc(buenas);
    cout<<"Obtuviste "<<porc<<"% de las preguntas correctas"<<endl;
}


int main(){

    int opciones;
    

    cout << "sobre que desea aprender?" << endl;
    cout << "1. vertebrados" << endl;
    cout << "2. moluscos" << endl;
    cout << "3. anelidos" << endl;
    cout << "4. nematodos" << endl;
    cout << "5. antropodos" << endl;
    cout << "6. salir" << endl;
    cin >> opciones;

    switch (opciones){
    case 1:
        cout << "vertebrados: son un subtipo de cordados los cuales se caracterizan por su espina dorsal.hay mas de 73.327 especies actualmente y ademas varios fosiles." << endl;
        cout << "Esta clasificacion de animales ha podido adaptarse a diversos tipos de ambientes, sin embargo vienen originalmente de aguas dulces, aunque muchas especies evolucionaron al mar y luego surgieron unos en el medio terrestre." << endl;
        cout << "ejemplos: ballenas, viboras, tiburones, gatos, seres humanos." << endl;
        cout << "Caracteristicas: simetria bilateral, craneo que protege al cerebro, esqueleto cartilago o oseo y por ultimo columna vertebral." << endl;
        cout << "" << endl;
        cout << "a continuacion le haremos un examen" << endl;
        cout << "Cargando examen"<<endl;
        examen_vertebrados();
        break;

    case 2:
        cout << "moluscos: son una especie invertebrada con simetria bilateral con cuerpo blando, desnudo o protegido por una concha o caparazon." << endl;
        cout << "Los moluscos son los invertebrados con mas numero de especies, despues de los artropodos." << endl;
        cout << "se calcula que hay entre 100,000 especies y 35,000 extintos. ejemplos:  almejas, ostras, calamares, pulpo, caracol." << endl;
        cout << "Caracteristicas: cuerpo blando, simetria bilateral, pueden estar protegidos por un caparros o concha." << endl;
        cout << "" << endl;
        cout << "a continuacion le haremos un examen" << endl;
        cout << "Cargando examen"<<endl;
        examen_moluscos();
        break;

    case 3:
        cout << "Phylum Annelida incluye gusanos segmentados. Estos animales se encuentran en habitats marinos, terrestres y de agua dulce, pero la presencia de agua o humedad es un factor critico para su supervivencia, especialmente en habitats terrestres." << endl;
        cout << "Incluye lombrices de tierra, gusanos poliquetos y sanguijuelas." << endl;
        cout << "" << endl;
        cout << "a continuacion le haremos un examen" << endl;
        cout << "Cargando examen"<<endl;
        examen_anelidos();
        break;

    case 4:
        cout << "Los nematodos no estan estrechamente relacionados con los verdaderos gusanos." << endl;
        cout << " Son insectos multicelulares con cuerpos lisos y no segmentados." << endl;
        cout << " Las especies de nematodos que se alimentan de plantas son tan pequeñas que se necesita un microscopio para verlas." << endl;
        cout << "Los adultos suelen verse largos y delgados, aunque algunas especies tienen forma de pera." << endl;
        cout << "" << endl;
        cout << "a continuacion le haremos un examen" << endl;
        cout << "Cargando examen"<<endl;
        examen_nematodos();
        break;

    case 5:
        cout << "Un artropodo es un animal invertebrado que tiene un exoesqueleto, un cuerpo segmentado y apéndices articulados emparejados." << endl;
        cout << " Los animales como un cangrejo, un escorpion y muchos otros son ejemplos de artropodos." << endl;
        cout << "Otra caracteristica de los artropodos es que tienen un cuerpo segmentado que ayuda a su movilidad." << endl;
        cout << "" << endl;
        cout << "a continuacion le haremos un examen" << endl;
        cout << "Cargando examen"<<endl;
        examen_antropodos();
        break;

    case 6:
        break;
    }
    return 0;
}
