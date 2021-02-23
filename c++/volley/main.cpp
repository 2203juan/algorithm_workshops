#include <iostream>
#include <string>
using namespace std;

int seleccion_multiple(){
    int contador = 0;

    //Pregunta 1
    cout<<"En el volleyball la red mide?"<<endl;
    cout<<endl;
    cout<<"a) Un metro de ancho y de 9,5 a 10 metros de largo."<<endl;
    cout<<"b) Dos metros de ancho y 6,5 a 8 metros de largo."<<endl;
    cout<<"c) Tres metros de ancho y 10 a 20 metros de largo."<<endl;

    string ans;

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "a")
        contador ++;

    //Pregunta 2
    cout<<"La red de volleyball tiene ?"<<endl;
    cout<<endl;
    cout<<"a) No cuenta con ninguna banda."<<endl;
    cout<<"b) Cuatro bandas en la parte superior."<<endl;
    cout<<"c) Dos bandas en la parte superior e inferior de la misma y tiene dos varillas verticales a cada lado."<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "c")
        contador ++;

    //Pregunta 3
    cout<<"El ataque debe ser?"<<endl;
    cout<<endl;
    cout<<"a) Por debajo de la red"<<endl;
    cout<<"b) Palmeo por encima de la red al campo contrario buscando lugares mal defendidos."<<endl;
    cout<<"c) Debe ser un palmeo entre nuestro equipo."<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "b")
        contador ++;

    //Pregunta 4
    cout<<"Se consigue un punto cuando ?"<<endl;
    cout<<endl;
    cout<<"a) El balón no pasa la red o se comete una falta"<<endl;
    cout<<"b) Los equipos llevan tres minutos con el balón en el aire."<<endl;
    cout<<"c) Todas las anteriores."<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "a")
        contador ++;

    //Pregunta 5
    cout<<"Después del saque, los jugadores pueden ocupar la posición que quieran dentro de sus campos?"<<endl;
    cout<<endl;
    cout<<"a) Si"<<endl;
    cout<<"b) No"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "a")
        contador ++;

    //Pregunta 6
    cout<<"Un equipo gana un set cuando ?"<<endl;
    cout<<endl;
    cout<<"a) Cuando sacan el balón de la cancha."<<endl;
    cout<<"b) Se cae el balón."<<endl;
    cout<<"c) Alcanza los 25 puntos antes que su rival"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "c")
        contador ++;

    //Pregunta 7
    cout<<"Con que se juega ?"<<endl;
    cout<<endl;
    cout<<"a) Las manos principalmente, aunque podemos utilizar cualquier parte del cuerpo (pie, codo, brazo, hombro, rodilla, cabeza)"<<endl;
    cout<<"b) Solo las piernas"<<endl;
    cout<<"c) Solo los brazos"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "a")
        contador ++;

    //Pregunta 8
    cout<<"Que partes del cuerpo Fortalece?"<<endl;
    cout<<endl;
    cout<<"a) Las rodillas porque permanecemos flexionados "<<endl;
    cout<<"b) Los músculos de las piernas, especialmente los glúteos y cuádriceps, los músculos de los pies, la zona lumbar y los hombros"<<endl;
    cout<<"c) Ninguna de las anteriores"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "b")
        contador ++;

    return contador;
}

int verdadero_falso(){
    int contador = 0;
    string ans = "";

    // Pregunta 9
    cout<<"Es un deporte que se juega con una pelota"<<endl;
    cout<<endl;
    cout<<"a) Verdadero"<<endl;
    cout<<"b) Falso"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "a")
        contador ++;

    // Pregunta 10
    cout<<"El balón puede caer a el piso"<<endl;
    cout<<endl;
    cout<<"a) Verdadero"<<endl;
    cout<<"b) Falso"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "b")
        contador ++;

    // Pregunta 11
    cout<<"Se juega con dos equipos"<<endl;
    cout<<endl;
    cout<<"a) Verdadero"<<endl;
    cout<<"b) Falso"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "a")
        contador ++;

    // Pregunta 12
    cout<<"Cada equipo tiene 10 personas y juegan en la cancha 4"<<endl;
    cout<<endl;
    cout<<"a) Verdadero"<<endl;
    cout<<"b) Falso"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "b")
        contador ++;

    // Pregunta 13
    cout<<"Los jugadores pueden pisar la línea final al sacar"<<endl;
    cout<<endl;
    cout<<"a) Verdadero"<<endl;
    cout<<"b) Falso"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "b")
        contador ++;

    // Pregunta 14
    cout<<"El balón tiene que pasar por encima de la red para que cuente como punto"<<endl;
    cout<<endl;
    cout<<"a) Verdadero"<<endl;
    cout<<"b) Falso"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "a")
        contador ++;

    // Pregunta 15
    cout<<"Durante el juego el balón tiene que ser golpeado continuamente, puede ser retenido y tomado por los jugadores."<<endl;
    cout<<endl;
    cout<<"a) Verdadero"<<endl;
    cout<<"b) Falso"<<endl;

    ans = "";

    cout<<"Ingresa tu respuesta : ";
    cin>>ans;
    cout<<endl;

    if (ans == "b")
        contador ++;

    return contador;
}

int main(){

    cout<<"Bienvenido al sistema"<<endl;
    cout<<"Ingresa tu nombre: ";
    string nombre;
    cin>>nombre;
    cout<<endl;
    cout<<"Genial "<<nombre<<"!!"<<endl;
    cout<<"Averiguemos que tanto sabes de volleyball"<<endl;
    cout<<endl;

    int multiples = seleccion_multiple();
    int verdaroOfalso = verdadero_falso();

    int tope = 7;

    int total = multiples + verdaroOfalso;

    cout<<nombre<<", tu puntuacion fue: "<<total<<"/15"<<endl;

    if (total > tope)
        cout<<"Has sido clasificado en el grupo B"<<endl;
    else
        cout<<"Has sido clasificado en el grupo A"<<endl;

    return 0;

}