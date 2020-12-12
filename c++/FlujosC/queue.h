#ifndef QUEUE_H_
#define QUEUE_H_
#include <stdlib.h>
#include <stdio.h>

struct node{
    int data;
    struct node *next;
};
typedef struct node node;


struct queue{
    int count;
    node *front;
    node *rear;
};
typedef struct queue queue;

void initialize(queue *q);

int isEmpty(queue *q);


void enqueue(queue *q, int value);

int dequeue(queue *q);


#endif 