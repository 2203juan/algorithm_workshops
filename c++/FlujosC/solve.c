#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include "queue.h"
#define min(a,b) a < b ? a: b
FILE *out;


int *path,*visitedDfs,*low,*ids,**rG,**G,V,id_n,*comps;


void dfs(int u,int parent){/*Tarjan BCC*/
    /*
    Esta es una implementación del algoritmo Tarjan BCC para encontrar los puntos
    de articulación (los que de eliminarse dejarían el grafo no conexo)
    */
    int v;
    visitedDfs[u] = 1;
    low[u] = ids[u] = id_n;
    id_n++;
    for(v = 0; v < V; v++){
        if(G[u][v] > 0 && v != parent){
            if(visitedDfs[v] == 0){
                dfs(v,u);
                low[u] = min(low[u],low[v]);
                if(ids[u] <= low[v])
                    comps[u] += 1;
                    

            }
            else
                low[u] = min(low[u],ids[v]);

        }
        
    }
}

void printPath(int v,int t){
    /*
    Esta funcion sirve para imprimir el camino ( requerido en el archivo pdf )
    */
    if(path[v] == -1)
        fprintf(out,"%d-",v+1);
    else{
        printPath(path[v],t);
        if(v != t)
            fprintf(out,"%d-",v+1);
        else
            fprintf(out,"%d: ",v+1);
        

    }

    
}

int bfs(int s,int t){
    /*
    Esta función implementa una busqueda en anchura sobre el grafo
    */
    int *visited,u,v,i;
    visited = malloc(V*(sizeof(int)));
    
    for(i = 0; i < V;i++)
        visited[i] = 0;
    
    queue *q;
    q = malloc(sizeof(queue));
    
    initialize(q);
    enqueue(q,s);
    
    
    visited[s] = 1;
    path[s] = -1;
    
        
    while(q->count > 0){
        u = dequeue(q);
        
        for(v = 0; v < V;v++){
            
            if(visited[v] == 0 && rG[u][v] > 0 ){
                enqueue(q,v);
                path[v] = u;
                visited[v] = 1;
            }
        }

    }
    return visited[t] == 1;

}

int fordFulkerson(int s, int t){
    /*
    Esta función implementa el algoritmo de fordFulkerson
    utilizado para calcular el flujo máximo
    */
    int u,v,ans = 0,path_flow;
    
    for(u = 0; u < V;u++)
        for(v = 0; v < V;v++)
            rG[u][v] = G[u][v];
   
  
    while(bfs(s,t)){
       path_flow = INT_MAX;
       v = t;
       while(v != s){
           
           u = path[v];
           path_flow = min(path_flow,rG[u][v]);
           v = path[v];
       }
       printPath(t,t);
       fprintf(out,"%d\n",path_flow);
       v = t;
       while(v != s){
           u = path[v];
           rG[u][v] -= path_flow;
           rG[v][u] += path_flow;
           v = path[v];
       }

       ans += path_flow;
   }

   return ans;
    
}

void solve(int s,int t){
    id_n = 0;
    int i,j,ans;
    ans = fordFulkerson(s,t);
    fprintf(out,"Total: %d\n\n",ans);
    for(i = 0; i < V;i++){/*Pasar el grafo a no dirigido*/
        for(j = 0; j < V;j++){
            if(G[i][j]> 0 ){
                G[j][i] = G[i][j] = 1;
            }

        }         

    }
                  
    fprintf(out,"Nodos criticos\n");
    for(i = 0; i < V;i++)
        if(visitedDfs[i] == 0) dfs(i,-1);
    for(i = 0; i < V;i++)
        if((comps[i] >= 1 && i != 0) || (comps[i] > 1 && i == 0)) fprintf(out,"%d ",i+1);
    fprintf(out,"\n");
}


int main(){
    FILE *inp;
    inp = fopen("entrada.in","r");
    out = fopen("salida.out","w");
    int s,t,i,j;
    
    
    
    if(inp != NULL){
        for(i = 0; i < 3;i++){
            if(i == 0)
                fscanf(inp,"%d",&V);
            else if(i == 1)
                fscanf(inp,"%d",&s);
            else
                fscanf(inp,"%d",&t);
        }
        s--;
        t--;
        /*printf("%d %d %d\n",V,s,t);*/
        G = malloc(V*sizeof(int *));
        rG = malloc(V*sizeof(int *));
        path = malloc(V*sizeof(int));
        visitedDfs = malloc(V*sizeof(int));
        low = malloc(V*sizeof(int));
        ids = malloc(V*sizeof(int));
        comps = malloc(V*sizeof(int));

        for(i = 0; i < V;i++){
            G[i] = malloc(V*sizeof(int));
            rG[i] = malloc(V*sizeof(int));
            visitedDfs[i] = 0;
            low[i] = 0;
            ids[i] = 0;
            comps[i] = 0;
        }
        for(i = 0; i < V;i++)
            for(j = 0; j < V;j++)
                G[i][j] = rG[i][j] = 0;
                

        for(i = 0; i < V;i++)
            for(j = 0; j < V;j++)
                fscanf(inp,"%d",&G[i][j]);
        /*
        for(i = 0; i < V;i++){
            for(j = 0; j < V;j++)
                printf("%d ",G[i][j]);
            
            printf("\n");
        }*/

        solve(s,t);
    }


    return 0;
}
