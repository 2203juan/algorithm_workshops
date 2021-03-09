

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    
    public static void solve(int N,int K,int cards[]){
    //la idea de solucion es simular el juego completo
        int points[] = new int[K],lo = 0,hi = N-1,i = 0,_max = -1;
        //se lleva registro en el arreglos points de cuantos puntos tiene cada jugador
        for(i = 0; i < K;i++) points[i] = 0;
        i = 0;
  
        ArrayList<Integer> ans = new ArrayList<Integer> ();
        while(lo <= hi){ //con lo se lleva la ultima carta disponible a la izquierda y con hi la ultima carta disponible a la derecha
            if(cards[lo] > cards[hi]){ //si tiene mas valor la carta de la izquierda llevo esa
                points[i] += cards[lo];
                lo += 1; //se aumenta lo simulando que se llevaron la carta
            }
            else{
                points[i] += cards[hi];
                hi -= 1; //se disminuye hi simulando que se llevaron la carta
            }
    
            i += 1; //el contador i es el que lleva el control de los turnos 
            if(i == K) i = 0; //si ya llegue al final reinicio el turno al primer jugador
        }
 
        for(i = 0; i < K; i++)
            _max = Math.max(_max, points[i]); //se revisa quien es el que tiene mayor puntaje
        
        for(i = 0; i < K;i++)
            if(points[i] == _max)//todos los que tengan ese maximo puntaje son los que imprimo
                    ans.add(i+1);
        
        for(i = 0; i < ans.size();i++){
            if(i+1 == ans.size())
                System.out.println(ans.get(i));
            else
                System.out.print(ans.get(i)+" ");      
        }
        
        
    }
    
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N,K,T,cards[],i,TC = 1;
        String line[];
        T = sc.nextInt();
        sc.nextLine();
       while(T-- > 0){
            line = sc.nextLine().split(" ");
            N = Integer.parseInt(line[0]);
            K = Integer.parseInt(line[1]);
            cards = new int[N];
            line = sc.nextLine().split(" ");
            for(i = 0; i < line.length;i++)
                cards[i] = Integer.parseInt(line[i]);
            System.out.println("Caso #"+TC+":");
            solve(N,K,cards);
            
            TC++;
            
            
            
        }
    }
    
}
