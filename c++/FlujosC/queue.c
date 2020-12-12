#include "queue.h"
#include <stdlib.h>
#include <stdio.h>



void initialize(queue *q){
    q->count = 0;
    q->front = NULL;
    q->rear = NULL;
}


int isEmpty(queue *q){
    return q->front == NULL;
}

void enqueue(queue *q, int value){
    node *tmp;
    tmp = malloc(sizeof(node));
    tmp->data = value;
    tmp->next = NULL;
    if(!isEmpty(q)){
        q->rear->next = tmp;
        q->rear = tmp;
    }
    else
        q->front = q->rear = tmp;
    
    q->count++;

   
}


int dequeue(queue *q){
    node *tmp;
    int n;
    if(!isEmpty(q)){
        n = q->front->data;
        tmp = q->front;
        q->front = q->front->next;
        q->count--;
         free(tmp);
        
    }
    
   
    return n;
}






