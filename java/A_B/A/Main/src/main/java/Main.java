
import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    
    public static Node agregar(Node raiz,int X){
        //el algoritmo inserta el nodo respetando el orden del arbol, si se llega a un nodo nulo es porque esa es la nueva posicion
        if (raiz == null)
            return new Node(X);
        else{
            if(raiz.data < X)//si aun no se llega a un nodo nulo, se verifica el nodo actual llamado raiz
                raiz.right = agregar(raiz.right,X);//si el valor de la raiz es menor a X significa que X debe ir a la derecha
            else
                raiz.left = agregar(raiz.left,X);//si el valor de la raiz es mayor a X significa que X debe ir a la izquierda
        }
        return raiz;
            
        
       
    }
    
  
    
    public static Boolean buscar(Node raiz,int v,ArrayList<Integer> camino){
        if(raiz != null){//esta es una busqueda binaria
            camino.add(raiz.data); //se va guardando el camino para encontrar el nodo v
            if(raiz.data == v)//si el valor del nodo actual es igual al de la raiz ya llegue, retorno true
                return true;
            else if(raiz.data < v) //si el valor que estoy buscando es mayor al valor del nodo actual voy hacia la derecha
                return buscar(raiz.right,v,camino);
            else
                return buscar(raiz.left,v,camino); //de lo contrario a la izquierda
        }
        else // si llegue a un nodo nulo retorno false
            return false;
    }
    
    public static int distancia(Node raiz,int X,int Y){
        int i;
        ArrayList<Integer> camino1 = new ArrayList<Integer> ();
        ArrayList<Integer> camino2 = new ArrayList<Integer>();
        Boolean band1 = buscar(raiz,X,camino1), band2 = buscar(raiz,Y,camino2); //se buscan ambos nodos
        
        
        if(band1 && band2){ //si ambos nodos estan procedo a buscar el primer nodo que encuentre distinto en ambos caminos
            i = 0;
            while(i < camino1.size() && i < camino2.size() && camino1.get(i) == camino2.get(i))
                i++;
           
            return camino1.size()+camino2.size()-2*i;
            
        }
        else
            return -1;
    }
    public static int ancestro(Node raiz,int U,int V){
        int i;
        ArrayList<Integer> camino1 = new ArrayList<Integer> ();
        ArrayList<Integer> camino2 = new ArrayList<Integer>();
        Boolean band1 = buscar(raiz,U,camino1), band2 = buscar(raiz,V,camino2); //misma idea del algoritmo de distancia
        if(band1 && band2){
            i = 0;
            while(i < camino1.size() && i < camino2.size() && camino1.get(i) == camino2.get(i)) //apenas difiera un nodo en el camino de ambos salgo del ciclo
                i++;
           
            return camino1.get(i-1);//el nodo anterior al cual ambos caminos dejaron de ser iguales es el ancestro
            
        }
        else
            return -1;
    }
    
    
    
    
    public static void main(String args[]){
        Node arbol = null;
        Scanner sc = new Scanner(System.in);
        int T,i,j,Q;
        String line[];
        T = sc.nextInt();
        for(i = 0; i < T;i++){
            arbol = null;
            Q = sc.nextInt();
            System.out.println("Caso #"+(i+1)+":\n");
            sc.nextLine();
            for(j = 0; j < Q;j++){
                line = sc.nextLine().split(" ");
                if(line[0].equals("agregar"))
                       arbol = agregar(arbol,Integer.parseInt(line[1]));
                else if(line[0].equals("distancia"))
                    System.out.println("distancia: "+distancia(arbol,Integer.parseInt(line[1]),Integer.parseInt(line[2]))+"\n");
                else
                    System.out.println("ancestro: "+ancestro(arbol,Integer.parseInt(line[1]),Integer.parseInt(line[2]))+"\n");
                
            }
            
        }
        
        
    }
    
}
