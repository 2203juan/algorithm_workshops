import java.util.*;
public class Main {
    public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	ArrayList<Integer> s = new ArrayList<Integer>();
    	int Q = sc.nextInt();//lee la cantidad de consultas
    	int tmp  = 0;
    	for(int i = 0; i < Q; i++) { // se itera Q veces
    		sc = new Scanner(System.in);
    		String line = sc.nextLine(); // se lee la consulta
    		long startTime = System.nanoTime();
    		if(line.length()==1) {// si es de un caracter
    			if (s.size() == 0) {// si la pila está vacía
    				System.out.println("No Food");
    			}
    			
    			else {// si la pila no está vacía
    				tmp = s.remove(s.size()-1);//eliminar el último
    				System.out.println(tmp);// mostrar el costo
    			}
    		}
    		
    		else {// si no es de un caracter
    			String[] parts = line.split(" ");// partir la linea en 2
    			int costo = Integer.parseInt(parts[1]);
    			s.add(costo);//añadir el costo a la pila (parts[1])
    		}
                long endTime = System.nanoTime();
                long timeElapsed = endTime - startTime;
                
                System.out.println("Tiempo de ejecución en milisegundos : " +
                                timeElapsed / (1000000.0));
    			
    	}
    	sc.close();
    }
}