#include <stdio.h>
int graph[103][103] = {0};
int BFSvisit[103][103] = {0};
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

struct Queue {
	int x;
	int y;
};

// int V: Starting point
// int N: X of Destination (-1)
// int M: Y of Destination (-1)
int BFS(int N, int M) {
	int i,k,popx,popy,x,y,front = 0,rear = 0,success = 0,distance = 0,qsize;
	struct Queue queue[10001];

	// Step #1. Starting point V
	queue[0].x = 0;
	queue[0].y = 0;
	rear++;
	BFSvisit[0][0] = 1;

	// Step #2. Loop while elements in the queue
	while(front<rear) {
		qsize = rear-front;
		for(k=0;k<qsize;k++) {
			popx = queue[front].x; // pop the first element
			popy = queue[front].y;	
			front++;
			if((popx == N-1) && (popy == M-1)) { // Step #3. If reaching the destination
				success = 1;
				return distance;
			}
			for(i=0;i<4;i++) { // Step #4. Check the adjacent nodes
				x = popx + dx[i];
				y = popy + dy[i];
				if(x<0||x>=N||y<0||y>=M) continue; // wall
				if(graph[x][y] == 1 && BFSvisit[x][y] == 0) {
					queue[rear].x = x;
					queue[rear].y = y;
					rear++;
					BFSvisit[x][y] = 1;
				}
			}
		}
		distance++;	
	}
	return distance;
}

int main(void){
	int N,M,i,j;
	scanf("%d %d",&N,&M);
	for(i=0;i<N;i++) {
		for(j=0;j<M;j++) {
			scanf("%1d",&graph[i][j]);
		}
	}
	//printf("complete scanf\n");

	printf("%d \n",BFS(N,M)+1);
	return 0;
}