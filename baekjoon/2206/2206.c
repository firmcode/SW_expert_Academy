#include <stdio.h>
int N,M;
int array[1005][1005];
int visited[1005][1005][2];
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
int queuex[2000005];
int queuey[2000005];
int queues[2000005];

int top,btm;


int BFS() {
	int cur_x,cur_y,cur_block;
	int next_x,next_y;


	while(top>btm)
	{
		//dequee
		cur_x = queuex[btm];
		cur_y = queuey[btm];
		cur_block = queues[btm];
		btm++;

		if(cur_x==N && cur_y==M)
			return visited[N][M][cur_block];

		for(int i=0 ;i<4;i++)
		{
			next_x = cur_x + dx[i];
			next_y = cur_y + dy[i];

			if(next_x > N || next_x < 1 || next_y > M || next_y < 1)
				continue;

			if(array[next_x][next_y]==0 && visited[next_x][next_y][cur_block]==0)
			{
				//enquee
				
				queuex[top]=next_x;
				queuey[top]=next_y;
				queues[top]=cur_block;
				top++;
				visited[next_x][next_y][cur_block] = visited[cur_x][cur_y][cur_block] + 1;
			}
			else if(array[next_x][next_y]==1 && cur_block==0)
			{
				//enquee
				//printf("enquee\n");
				queuex[top]=next_x;
				queuey[top]=next_y;
				queues[top]=1;
				top++;
				visited[next_x][next_y][1] = visited[cur_x][cur_y][0] + 1;
			}

		}
	}
	return -2;
}

int main(void) {
	int i,j;
	scanf("%d %d",&N,&M);
	for(i=1;i<=N;i++) {
		for(j=1;j<=M;j++) {
			scanf("%1d",&array[i][j]);
		}
	}
	/*
	for(i=1;i<=N;i++) {
		for(j=1;j<=M;j++) {
			printf("%d",array[i][j]);
		}
		printf("\n");
	}*/

	top=1;
	btm=0;
	queuex[0]=1;
	queuey[0]=1;

	printf("%d \n",BFS()+1);
	return 0;
}