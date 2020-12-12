#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Cancion{
    char *nombre;
    double duracion;
    int anioLanzamiento;


} Cancion;


typedef struct Integrante{
    char *nombre;
    char *paisOrigen;
    char *rol;
    
}Integrante;


typedef struct Banda{
    char *nombre;
    char *paisOrigen;
    int cantidadCanciones;
    Cancion *canciones;
    int cantidadIntegrantes;
    Integrante *integrantes;
}Banda;

void limpiarBuffer(){
    fflush(stdin);
    //while((getchar()) == '\n'); /*para tomar los espacios de linea despues del scanf*/
    int ch;
    while ((ch = fgetc(stdin)) != '\n' && ch != EOF);
    fflush(stdin);
}

int esMinuscula(char c){
    /*
    Retorna 1 si el caracter c que se recibe en el parametro es una letra minuscula, de lo contrario 0
    */
    return (int)c >= 97 && (int)c <= 122;
}

int esMayuscula(char c){
    /*
    Retorna 1 si el caracter c que se recibe en el parametro es una letra mayuscula, de lo contrario 0
    */
    return  ((int)c >= 65 && (int)c <= 90);

}




void pasarAMayuscula(char *s){
    /*
    Pasa las letras minusculas a mayusculas
    */
    int i;
    for(i = 0; s[i] != '\0';i++)
        if(esMinuscula(s[i]))
            s[i] = ((int)s[i])-32; /*restarle 32 al codigo ascii para dejarlo en mayuscula*/
    
}


void pasarAMinuscula(char *s){
    /*
    Pasa las letras mayusculas a minusculas
    */
    int i;
    for(i = 0; s[i] != '\0';i++)
        if(esMayuscula(s[i]))
            s[i] = ((int)s[i])+32; /*sumarle 32 al codigo ascii para dejarlo en minuscula*/
    
}

int buscarEspacio(int *bandasUsadas){ /*Busca un espacio para asignarlo a una nueva banda*/
    int i;
    for(i = 0; i < 20;i++)
        if(bandasUsadas[i] == 0) return i;
    return -1;
}

void agregarBanda(Banda *bandas, int *bandasUsadas){
    char *s;
    int pos,i;
    pos = buscarEspacio(bandasUsadas);
    if(pos == -1)
        printf("No hay mas espacio para bandas!\n");
    else{
        printf("Ingrese el nombre de la banda\n");
        bandas[pos].nombre = malloc(255*sizeof(char));
        limpiarBuffer();
        scanf("%255[^\n]", bandas[pos].nombre);
        
        pasarAMayuscula(bandas[pos].nombre);
        printf("Ingres el pais de origen\n");
        bandas[pos].paisOrigen = malloc(255*sizeof(char));

        limpiarBuffer();
        scanf("%255[^\n]", bandas[pos].paisOrigen);
        printf("Ingrese la cantidad de canciones\n");
        limpiarBuffer();
        scanf("%d",&bandas[pos].cantidadCanciones);
        while(bandas[pos].cantidadCanciones > 30 || bandas[pos].cantidadCanciones < 0){
            printf("Ingrese cantidad de canciones entre 0 y 30!\n");
            scanf("%d",&bandas[pos].cantidadCanciones);
        }

        printf("Ingrese la cantidad de integrantes\n");
        scanf("%d",&bandas[pos].cantidadIntegrantes);
        while(bandas[pos].cantidadIntegrantes > 10 || bandas[pos].cantidadIntegrantes <= 0){
            printf("Ingrese cantidad de integrantes entre 1 y 10!\n");
            scanf("%d",&bandas[pos].cantidadIntegrantes);
        }
        
        bandas[pos].canciones = malloc(bandas[pos].cantidadCanciones*sizeof(Cancion));
        for(i = 0; i <bandas[pos].cantidadCanciones;i++){
            bandas[pos].canciones[i].nombre = malloc(255*sizeof(char));
            printf("Ingrese el nombre de la cancion\n");
            limpiarBuffer();
            scanf("%255[^\n]", bandas[pos].canciones[i].nombre);
            limpiarBuffer();
            pasarAMinuscula(bandas[pos].canciones[i].nombre);
            printf("Ingrese la duracion\n");
          
            scanf("%lf",&bandas[pos].canciones[i].duracion);
            printf("Ingrese año de lanzamiento\n");
            
            scanf("%d",&bandas[pos].canciones[i].anioLanzamiento);
            
        }
       
        
        bandas[pos].integrantes = malloc(bandas[pos].cantidadIntegrantes*sizeof(Integrante));
        for(i = 0; i < bandas[pos].cantidadIntegrantes;i++){
            bandas[pos].integrantes[i].nombre = malloc(255*sizeof(char));
            printf("Ingrese el nombre del integrante\n");
            limpiarBuffer();
            scanf("%255[^\n]", bandas[pos].integrantes[i].nombre);
            
            
            printf("Ingres el pais de origen\n");
            limpiarBuffer();
            bandas[pos].integrantes[i].paisOrigen = malloc(255*sizeof(char));
            scanf("%255[^\n]", bandas[pos].integrantes[i].paisOrigen);
            
            printf("Ingrese rol del integrante\n");
            limpiarBuffer();
            bandas[pos].integrantes[i].rol = malloc(255*sizeof(char));
            scanf("%255[^\n]", bandas[pos].integrantes[i].rol);
            //limpiarBuffer();

        }


        bandasUsadas[pos] = 1;
    }

}

void mostrarBandas(Banda *bandas,int *bandasUsadas){
    int i;
    for(i = 0; i < 20;i++){
        if(bandasUsadas[i] == 1){
            printf("Nombre de la banda: %s\n",bandas[i].nombre);
            printf("Pais de origen de la banda: %s\n",bandas[i].paisOrigen);     
            printf("Cantidad de canciones de la banda: %d\n",bandas[i].cantidadCanciones);
            printf("Cantidad de integrantes de la banda: %d\n\n",bandas[i].cantidadIntegrantes);
               
        }
    }
}

void mostrarIntegrantes(Integrante *integrantes,int N){
    int i;
    for(i = 0; i < N;i++){
        printf("Integrante %d\n",i+1);
        printf("Nombre: %s\n",integrantes[i].nombre);
        printf("Pais de origen: %s\n",integrantes[i].paisOrigen);
        printf("Rol: %s\n\n",integrantes[i].rol);
    }
}

void mostrarCanciones(Cancion *canciones,int N){
    int i;
    for(i = 0; i < N;i++){
        printf("Cancion %d\n",i+1);
        printf("Nombre: %s\n",canciones[i].nombre);
        printf("Año de lanzamiento: %d\n",canciones[i].anioLanzamiento);
        printf("Duracion: %lf\n\n",canciones[i].duracion);
    }
}

void mostrarBanda(Banda *bandas,int *bandasUsadas,char *s){
    int i;
    for(i = 0; i < 20; i++){
        if(bandasUsadas[i] == 1 && strcmp(bandas[i].nombre,s) == 0){
            printf("Nombre de la banda: %s\n",bandas[i].nombre);
            printf("Pais de origen de la banda: %s\n",bandas[i].paisOrigen);     
            printf("Cantidad de canciones de la banda: %d\n",bandas[i].cantidadCanciones);
            printf("Cantidad de integrantes de la banda: %d\n",bandas[i].cantidadIntegrantes);
            mostrarIntegrantes(bandas[i].integrantes,bandas[i].cantidadIntegrantes);
            mostrarCanciones(bandas[i].canciones,bandas[i].cantidadCanciones);
            break;
        }
    }

}

void eliminarBanda(Banda *bandas,int *bandasUsadas,char *s){
    int i;
    for(i = 0; i < 20;i++){
        if(bandasUsadas[i] == 1 && strcmp(bandas[i].nombre,s) == 0){
            bandasUsadas[i] = 0;
            break;
        }
    }
}


double maxDuracion(Cancion *canciones,int N){
    int i;
    double maxD = 0.0;
    for(i = 0; i < N;i++){
        if(canciones[i].duracion > maxD)
            maxD = canciones[i].duracion;

    }
    return maxD;

}

void imprimirCancionLarga(double maxD,Cancion *canciones,int N){
    int i;
    for(i = 0; i < N;i++){
        if(canciones[i].duracion == maxD){
            printf("Nombre: %s\n",canciones[i].nombre);
            printf("Año de lanzamiento: %d\n",canciones[i].anioLanzamiento);
            printf("Duracion: %lf\n\n",canciones[i].duracion);

        }
    }
}
void cancionMasLarga(Banda *bandas,int *bandasUsadas){
    double maxD = 0.0,resMaxD;
    int i;
    for(i = 0; i < 20; i++){
        if(bandasUsadas[i] == 1){
            resMaxD = maxDuracion(bandas[i].canciones,bandas[i].cantidadCanciones);
            if(resMaxD > maxD)
                maxD = resMaxD;

        }
    }
    for(i = 0; i < 20;i++){
        if(bandasUsadas[i] == 1)
            imprimirCancionLarga(maxD,bandas[i].canciones,bandas[i].cantidadCanciones);
        
    }

}

double duracionTotalCanciones(Cancion *canciones, int N){
    double duracion = 0.0;
    int i;
    for(i = 0; i < N;i++)
        duracion += canciones[i].duracion;
    return duracion;

}

void mostrarBandasYDuracion(Banda *bandas,int *bandasUsadas){
    int i;
    for(i = 0; i < 20;i++){
        if(bandasUsadas[i] == 1 ){
            printf("Nombre de la banda: %s\n",bandas[i].nombre);
            printf("Pais de origen de la banda: %s\n",bandas[i].paisOrigen);     
            printf("Cantidad de canciones de la banda: %d\n",bandas[i].cantidadCanciones);
            printf("Cantidad de integrantes de la banda: %d\n",bandas[i].cantidadIntegrantes);
            printf("Duracion total de sus canciones: %lf\n\n",duracionTotalCanciones(bandas[i].canciones,bandas[i].cantidadCanciones));

        }
    }

}

void mystrcpy( char* _dst, const char* _src ){
   while((*_dst++ = *_src++));
   fflush(stdin);
}


int main(){
    int opc = 1,i,ch;
    char s[255];
    //scanf("%s", s);

   
    //printf("%s\n",s);
    //Banda bandas[20];
    Banda *bandas = malloc(20*(sizeof(Banda)));
    int bandasUsadas[20];
    for(i = 0; i < 20;i++) bandasUsadas[i] = 0;

/*
typedef struct Banda{
    char *nombre;
    char *paisOrigen;
    int cantidadCanciones;
    Cancion *canciones;
    int cantidadIntegrantes;
    Integrante *integrantes;
}Banda;


*/
    /*
    //Inicializamos la banda 0 y la banda 1
    bandas[0].integrantes = malloc(bandas[0].cantidadIntegrantes*sizeof(Integrante));
    bandas[1].integrantes = malloc(bandas[1].cantidadIntegrantes*sizeof(Integrante));

    bandas[0].canciones = malloc(bandas[0].cantidadCanciones*sizeof(Cancion));
    bandas[1].canciones = malloc(bandas[1].cantidadCanciones*sizeof(Cancion));

    bandas[0].cantidadCanciones = 4;
    bandas[1].cantidadCanciones = 4;

    bandas[0].cantidadIntegrantes = 2;
    bandas[1].cantidadIntegrantes = 2;

    bandas[0].nombre = malloc(255*sizeof(char));
    mystrcpy(bandas[0].nombre ,"ZION Y LENOX");
    
    bandas[0].paisOrigen = malloc(255*sizeof(char));
    mystrcpy(bandas[0].paisOrigen ,"Puerto Rico");

    bandas[1].nombre = malloc(255*sizeof(char));
    mystrcpy(bandas[1].nombre ,"MAU Y RICKY");
    
    bandas[1].paisOrigen = malloc(255*sizeof(char));
    mystrcpy(bandas[1].paisOrigen ,"Venezuela");
    //agregamos los integrantes de la banda 0
    //integrante 0

    //nombre
    bandas[0].integrantes[0].nombre = malloc(255*sizeof(char));
    mystrcpy(bandas[0].integrantes[0].nombre,"Zion");

    // pais de origen
    bandas[0].integrantes[0].paisOrigen = malloc(255*sizeof(char));
    mystrcpy(bandas[0].integrantes[0].paisOrigen,"Puerto Rico");

    //rol
    bandas[0].integrantes[0].rol = malloc(255*sizeof(char));
    mystrcpy(bandas[0].integrantes[0].rol,"vocalista");

    //ntegrante 1
    //nombre
    bandas[0].integrantes[1].nombre = malloc(255*sizeof(char));
    mystrcpy(bandas[0].integrantes[1].nombre,"Lenox");

    //pais de origen
    bandas[0].integrantes[1].paisOrigen = malloc(255*sizeof(char));
    mystrcpy(bandas[0].integrantes[1].paisOrigen,"Puerto Rico");

    //rol
    bandas[0].integrantes[1].rol = malloc(255*sizeof(char));
    mystrcpy(bandas[0].integrantes[1].rol , "vocalista");



    //agregamos los integrantes de la banda 1
    //nombre
    bandas[1].integrantes[0].nombre = malloc(255*sizeof(char));
    mystrcpy(bandas[1].integrantes[0].nombre,"Mau");

    //pais de origen
    bandas[1].integrantes[0].paisOrigen = malloc(255*sizeof(char));
    mystrcpy(bandas[1].integrantes[0].paisOrigen,"Puerto Rico");

    //rol
    bandas[1].integrantes[0].rol = malloc(255*sizeof(char));
    mystrcpy(bandas[1].integrantes[0].rol,"vocalista");

    //nombre
    bandas[1].integrantes[1].nombre = malloc(255*sizeof(char));
    mystrcpy(bandas[1].integrantes[1].nombre, "Ricky");

    //pais de origen
    bandas[1].integrantes[1].paisOrigen = malloc(255*sizeof(char));
    mystrcpy(bandas[1].integrantes[1].paisOrigen, "Puerto Rico");

    //rol
    bandas[1].integrantes[1].rol = malloc(255*sizeof(char));
    mystrcpy(bandas[1].integrantes[1].rol,"vocalista");


    //agregamos las canciones de la banda 0
    bandas[0].canciones[0].nombre = malloc(255*sizeof(char));
    bandas[0].canciones[1].nombre = malloc(255*sizeof(char));
    bandas[0].canciones[2].nombre = malloc(255*sizeof(char));
    bandas[0].canciones[3].nombre = malloc(255*sizeof(char));

    mystrcpy(bandas[0].canciones[0].nombre , "llamame");
    mystrcpy(bandas[0].canciones[1].nombre , "lunes");
    mystrcpy(bandas[0].canciones[2].nombre , "te amo");
    mystrcpy(bandas[0].canciones[3].nombre , "dia cinco");


    bandas[0].canciones[0].duracion = 205;
    bandas[0].canciones[1].duracion = 308;
    bandas[0].canciones[2].duracion = 187;
    bandas[0].canciones[3].duracion = 425;

    bandas[0].canciones[0].anioLanzamiento = 2020;
    bandas[0].canciones[1].anioLanzamiento = 2015;
    bandas[0].canciones[2].anioLanzamiento = 2019;
    bandas[0].canciones[3].anioLanzamiento = 2012;

    //agregamos las canciones de la banda 1
    bandas[1].canciones[0].nombre = malloc(255*sizeof(char));
    bandas[1].canciones[1].nombre = malloc(255*sizeof(char));
    bandas[1].canciones[2].nombre = malloc(255*sizeof(char));
    bandas[1].canciones[3].nombre = malloc(255*sizeof(char));

    strcpy(bandas[1].canciones[0].nombre , "desconocidos");
    strcpy(bandas[1].canciones[1].nombre , "papas");
    strcpy(bandas[1].canciones[2].nombre , "no llores");
    strcpy(bandas[1].canciones[3].nombre , "besandote");


    bandas[1].canciones[0].duracion = 250;
    bandas[1].canciones[1].duracion = 524;
    bandas[1].canciones[2].duracion = 95;
    bandas[1].canciones[3].duracion = 432;

    bandas[1].canciones[0].anioLanzamiento = 2019;
    bandas[1].canciones[1].anioLanzamiento = 2017;
    bandas[1].canciones[2].anioLanzamiento = 2018;
    bandas[1].canciones[3].anioLanzamiento = 2013;

    bandasUsadas[0] = 1;
    bandasUsadas[1] = 1;
    */


    while(opc != 0){
        printf("Ingrese 0 para salir\n");
        printf("Ingrese 1 para agregar una nueva banda\n");
        printf("Ingrese 2 para mostrar informacion de bandas\n");
        printf("Ingrese 3 para mostrar banda\n");
        printf("Ingrese 4 para eliminar banda\n");
        printf("Ingrese 5 para mostrar la informacion de la cancion mas larga\n");
        printf("Ingrese 6 para mostrar las bandas y el tiempo total de canciones\n");
        scanf("%d",&opc);
        
        if(opc == 1)
            agregarBanda(bandas,bandasUsadas);
        else if(opc == 2)
            mostrarBandas(bandas,bandasUsadas);
        else if(opc == 3){
            printf("Ingrese el nombre de la banda que desea buscar\n");
             limpiarBuffer();
            scanf("%255[^\n]", s);
           limpiarBuffer();
            pasarAMayuscula(s);
            mostrarBanda(bandas,bandasUsadas,s);

            
        }
        else if(opc == 4){
            printf("Ingrese el nombre de la banda que desea eliminar\n");
            limpiarBuffer();
            scanf("%255[^\n]", s);
            limpiarBuffer();
            pasarAMayuscula(s);
            eliminarBanda(bandas,bandasUsadas,s);

        }
        else if(opc == 5)
            cancionMasLarga(bandas,bandasUsadas);

        else if(opc == 6)
            mostrarBandasYDuracion(bandas,bandasUsadas);
        

        


        

    }

    return 0;
}