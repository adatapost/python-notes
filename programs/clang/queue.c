#include <stdio.h>

void push(int queue[],int item) ;
int pop(int queue[]);

int top = -1, front = -1;
void push(int queue[],int item)
{
   top++;
   if(top == 0)
     front = 0;
   queue[top] = item;
}
int pop(int queue[])
{
   return queue[front++];
}
int main()
{
    int q[5];  /* 10 20  30 */
    push(q,10);
    push(q, 20);
    push(q, 30);

    
    return 0;
}