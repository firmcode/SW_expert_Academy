#include <stdio.h>
int queue[100001];
int visited[100001] = {0};
int front = 0, rear = 0, qsize, distance = 0;
int BFS(int N, int K){
	int pop,i;
	visited[N] = 1;
	queue[rear] = N;
	rear++;
	while(front < rear) {
		qsize = rear - front;
		for(i=0;i<qsize;i++) {
			pop = queue[front];
			front++;
			if(pop == K) return distance;
			if(pop+1 <= 100000 && visited[pop+1] == 0) {
				queue[rear] = pop+1;
				rear++;
				visited[pop+1] = 1;
			}
			if(pop-1 >= 0 && visited[pop-1] == 0) {
				queue[rear] = pop-1;
				rear++;
				visited[pop-1] = 1;
			}	
			if(pop*2 <= 100000 && visited[pop*2] == 0) {
				queue[rear] = pop*2;
				rear++;
				visited[pop*2] = 1;
			}	
		}
		distance++;
	}
	return 0;
}


int main(void) {
	int N,K;
	scanf("%d %d",&N,&K);
	printf("%d \n",BFS(N,K));
	return 0;
}
