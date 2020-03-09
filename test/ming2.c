#include <stdio.h>
int N,M;
int redx,redy,bluex,bluey;

char array[15][15];
int bvisit[15][15];
int rvisit[15][15];
int visit[15][15][15][15];

int bqueuex[100005];
int bqueuey[100005];
int rqueuex[100005];
int rqueuey[100005];

int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};

int BFS() {
	int front=0,rear=0,qsize,k;
	int i,j,count=1;
	int rpopx,rpopy,bpopx,bpopy;
	int rnextx,rnexty,bnextx,bnexty;

	//rvisit[redx][redy] = 1;
	//bvisit[bluex][bluey] = 1;	
	visit[redx][redy][bluex][bluey] = 1;

	rqueuex[rear] = redx;
	rqueuey[rear] = redy;
	bqueuex[rear] = bluex;
	bqueuey[rear] = bluey;
	rear++;

	while(front < rear) {
		qsize = rear - front;
		for(k=0;k<qsize;k++) {

			// 현재 위치 pop
			rpopx = rqueuex[front];
			rpopy = rqueuey[front];
			bpopx = bqueuex[front];
			bpopy = bqueuey[front];
			front++;

			{ // 오른쪽 이동 
				bnextx = bpopx;
				bnexty = bpopy;
				rnextx = rpopx;
				rnexty = rpopy;

				array[rpopx][rpopy] = 'R';
				array[bpopx][bpopy] = 'B';
				
				printf("************count: %d***************\n",count);
				for(i=0;i<N;i++) {
					for(j=0;j<M;j++) {
						printf("%c ",array[i][j]);
					}
					printf("\n");
				}

				if(rpopy < bpopy) { // blue부터 이동
					while(1) {
						bnexty = bnexty + dy[0];
						if(array[bnextx][bnexty]=='.') { // 이동
							array[bnextx][bnexty-dy[0]] = '.';
							array[bnextx][bnexty] = 'B';
						}
						else if(array[bnextx][bnexty]=='O') { // 구멍 빠짐
							array[bnextx][bnexty-dy[0]] = '.';
							bnextx = -1;
							bnexty = -1;
							break;
						}
						else {
							bnexty = bnexty - dy[0];
							break;
						}
					}

					while(1) {
						rnexty = rnexty + dy[0];
						if(array[rnextx][rnexty]=='.') { // 이동
							array[rnextx][rnexty-dy[0]] = '.';
							array[rnextx][rnexty] = 'R';						
						}
						else if(array[rnextx][rnexty]=='O') { // 구멍 빠짐
							array[rnextx][rnexty-dy[0]] = '.';
							rnextx = -1;
							rnexty = -1;
							break;
						}
						else {
							rnexty = rnexty - dy[0];
							break;
						}
					}										
				}
				else {
					while(1) {
						rnexty = rnexty + dy[0];
						if(array[rnextx][rnexty]=='.') { // 이동
							array[rnextx][rnexty-dy[0]] = '.';
							array[rnextx][rnexty] = 'R';						
						}
						else if(array[rnextx][rnexty]=='O') { // 구멍 빠짐
							array[rnextx][rnexty-dy[0]] = '.';
							rnextx = -1;
							rnexty = -1;
							break;
						}
						else {
							rnexty = rnexty - dy[0];
							break;
						}
					}	

					while(1) {
						bnexty = bnexty + dy[0];
						if(array[bnextx][bnexty]=='.') { // 이동
							array[bnextx][bnexty-dy[0]] = '.';
							array[bnextx][bnexty] = 'B';
						}
						else if(array[bnextx][bnexty]=='O') { // 구멍 빠짐
							array[bnextx][bnexty-dy[0]] = '.';
							bnextx = -1;
							bnexty = -1;
							break;
						}
						else {
							bnexty = bnexty - dy[0];
							break;
						}
					}										
				}

				if(rnextx==-1 && rnexty==-1 && bnextx!=-1) { // 파란공은 구멍에 안빠지고 빨간 공만 빠졌을 때
					return count;
				}

				//if((bnextx!=-1)&&(bvisit[bnextx][bnexty]==0 || rvisit[rnextx][rnexty] == 0 || bvisit[bnextx][bnexty]!=rvisit[rnextx][rnexty])) {
				if((bnextx!=-1)&&(visit[rnextx][rnexty][bnextx][bnexty]==0)) {

					// 파란 공은 구멍에 안빠지고 이전에 방문한 상태가 아닐 때

					printf("> 오른쪽 이동 큐 삽입 \n");
					for(i=0;i<N;i++) {
						for(j=0;j<M;j++) {
							printf("%c ",array[i][j]);
						}
						printf("\n");
					}
					visit[rnextx][rnexty][bnextx][bnexty] = count;
					//bvisit[bnextx][bnexty] = count;	
					//rvisit[rnextx][rnexty] = count;	
					bqueuex[rear] = bnextx;
					bqueuey[rear] = bnexty;
					rqueuex[rear] = rnextx;
					rqueuey[rear] = rnexty;
					rear++;									
				}
				printf("test!!! %d %d\n", bnextx,bnexty);
				for(i=0;i<N;i++) {
						for(j=0;j<M;j++) {
							printf("%c ",array[i][j]);
						}
						printf("\n");
					}


				if(bnextx!=-1) array[bnextx][bnexty]='.'; // 인덱스 에러 방지
				if(rnextx!=-1) array[rnextx][rnexty]='.';

			}
	
			{ // 왼쪽 이동 
				bnextx = bpopx;
				bnexty = bpopy;
				rnextx = rpopx;
				rnexty = rpopy;

				array[rpopx][rpopy] = 'R';
				array[bpopx][bpopy] = 'B';

				if(rpopy > bpopy) { // blue부터 이동
					while(1) {
						bnexty = bnexty + dy[1];
						if(array[bnextx][bnexty]=='.') { // 이동
							array[bnextx][bnexty-dy[1]] = '.';
							array[bnextx][bnexty] = 'B';
						}
						else if(array[bnextx][bnexty]=='O') { // 구멍 빠짐
							array[bnextx][bnexty-dy[1]] = '.';
							bnextx = -1;
							bnexty = -1;
							break;
						}
						else {
							bnexty = bnexty - dy[1];
							break;
						}
					}

					while(1) {
						rnexty = rnexty + dy[1];
						if(array[rnextx][rnexty]=='.') { // 이동
							array[rnextx][rnexty-dy[1]] = '.';
							array[rnextx][rnexty] = 'R';						
						}
						else if(array[rnextx][rnexty]=='O') { // 구멍 빠짐
							array[rnextx][rnexty-dy[1]] = '.';
							rnextx = -1;
							rnexty = -1;
							break;
						}
						else {
							rnexty = rnexty - dy[1];
							break;
						}
					}						
				}
				else {
					while(1) {
						rnexty = rnexty + dy[1];
						if(array[rnextx][rnexty]=='.') { // 이동
							array[rnextx][rnexty-dy[1]] = '.';
							array[rnextx][rnexty] = 'R';						
						}
						else if(array[rnextx][rnexty]=='O') { // 구멍 빠짐
							array[rnextx][rnexty-dy[1]] = '.';
							rnextx = -1;
							rnexty = -1;
							break;
						}
						else {
							rnexty = rnexty - dy[1];
							break;
						}
					}	

					while(1) {
						bnexty = bnexty + dy[1];
						if(array[bnextx][bnexty]=='.') { // 이동
							array[bnextx][bnexty-dy[1]] = '.';
							array[bnextx][bnexty] = 'B';
						}
						else if(array[bnextx][bnexty]=='O') { // 구멍 빠짐
							array[bnextx][bnexty-dy[1]] = '.';
							bnextx = -1;
							bnexty = -1;
							break;
						}
						else {
							bnexty = bnexty - dy[1];
							break;
						}
					}										
				}

				if(rnextx==-1 && rnexty==-1 && bnextx!=-1) {
					return count;
				}

				//if((bnextx!=-1)&&(bvisit[bnextx][bnexty]==0 || rvisit[rnextx][rnexty] == 0 || bvisit[bnextx][bnexty]!=rvisit[rnextx][rnexty]))  {
				if((bnextx!=-1)&&(visit[rnextx][rnexty][bnextx][bnexty]==0)) {
					printf("> 왼쪽 이동 큐 삽입 M : %d \n",M);
					for(i=0;i<N;i++) {
						for(j=0;j<M;j++) {
							printf("%d %d %c ",i,j,array[i][j]);
						}
						printf("\n");	
					}	
					visit[rnextx][rnexty][bnextx][bnexty] = count;		
					//bvisit[bnextx][bnexty] = count;	
					//rvisit[rnextx][rnexty] = count;	
					bqueuex[rear] = bnextx;
					bqueuey[rear] = bnexty;
					rqueuex[rear] = rnextx;
					rqueuey[rear] = rnexty;
					rear++;									
				}

				if(bnextx!=-1) array[bnextx][bnexty]='.';
				if(rnextx!=-1) array[rnextx][rnexty]='.';

			}

			{ // 위쪽 이동 
				bnextx = bpopx;
				bnexty = bpopy;
				rnextx = rpopx;
				rnexty = rpopy;		

				array[rpopx][rpopy] = 'R';
				array[bpopx][bpopy] = 'B';

				if(rpopx > bpopx) { // blue부터 이동
					while(1) {
						bnextx = bnextx + dx[2];
						if(array[bnextx][bnexty]=='.') { // 이동
							array[bnextx-dx[2]][bnexty] = '.';
							array[bnextx][bnexty] = 'B';
						}
						else if(array[bnextx][bnexty]=='O') { // 구멍 빠짐
							array[bnextx-dx[2]][bnexty] = '.';
							bnextx = -1;
							bnexty = -1;
							break;
						}
						else {
							bnextx = bnextx - dx[2];
							break;
						}
					}

					while(1) {
						rnextx = rnextx + dx[2];
						if(array[rnextx][rnexty]=='.') { // 이동
							array[rnextx-dx[2]][rnexty] = '.';
							array[rnextx][rnexty] = 'R';						
						}
						else if(array[rnextx][rnexty]=='O') { // 구멍 빠짐
							array[rnextx-dx[2]][rnexty] = '.';
							rnextx = -1;
							rnexty = -1;
							break;
						}
						else {
							rnextx = rnextx - dx[2];
							break;
						}
					}						
				}
				else {
					while(1) {
						rnextx = rnextx + dx[2];
						if(array[rnextx][rnexty]=='.') { // 이동
							array[rnextx-dx[2]][rnexty] = '.';
							array[rnextx][rnexty] = 'R';						
						}
						else if(array[rnextx][rnexty]=='O') { // 구멍 빠짐
							array[rnextx-dx[2]][rnexty] = '.';
							rnextx = -1;
							rnexty = -1;
							break;
						}
						else {
							rnextx = rnextx - dx[2];
							break;
						}
					}	

					while(1) {
						bnextx = bnextx + dx[2];
						if(array[bnextx][bnexty]=='.') { // 이동
							array[bnextx-dx[2]][bnexty] = '.';
							array[bnextx][bnexty] = 'B';
						}
						else if(array[bnextx][bnexty]=='O') { // 구멍 빠짐
							array[bnextx-dx[2]][bnexty] = '.';
							bnextx = -1;
							bnexty = -1;
							break;
						}
						else {
							bnextx = bnextx - dx[2];
							break;
						}
					}										
				}

				if(rnextx==-1 && rnexty==-1 && bnextx!=-1) {
					return count;
				}

				//if((bnextx!=-1)&&(bvisit[bnextx][bnexty]==0 || rvisit[rnextx][rnexty] == 0 || bvisit[bnextx][bnexty]!=rvisit[rnextx][rnexty]))  {
				if((bnextx!=-1)&&(visit[rnextx][rnexty][bnextx][bnexty]==0)) {
					printf("> 위쪽 이동 큐 삽입 \n");
					for(i=0;i<N;i++) {
						for(j=0;j<M;j++) {
							printf("%c ",array[i][j]);
						}
						printf("\n");	
					}
					visit[rnextx][rnexty][bnextx][bnexty] = count;
					//bvisit[bnextx][bnexty] = count;	
					//rvisit[rnextx][rnexty] = count;	
					bqueuex[rear] = bnextx;
					bqueuey[rear] = bnexty;
					rqueuex[rear] = rnextx;
					rqueuey[rear] = rnexty;
					rear++;									
				}

				if(bnextx!=-1) array[bnextx][bnexty]='.';
				if(rnextx!=-1) array[rnextx][rnexty]='.';	
		
			}

			{ // 아래쪽 이동 
				bnextx = bpopx;
				bnexty = bpopy;
				rnextx = rpopx;
				rnexty = rpopy;		

				array[rpopx][rpopy] = 'R';
				array[bpopx][bpopy] = 'B';

				if(rpopx < bpopx) { // blue부터 이동
					while(1) {
						bnextx = bnextx + dx[3];
						if(array[bnextx][bnexty]=='.') { // 이동
							array[bnextx-dx[3]][bnexty] = '.';
							array[bnextx][bnexty] = 'B';
						}
						else if(array[bnextx][bnexty]=='O') { // 구멍 빠짐
							array[bnextx-dx[3]][bnexty] = '.';
							bnextx = -1;
							bnexty = -1;
							break;
						}
						else {
							bnextx = bnextx - dx[3];
							break;
						}
					}

					while(1) {
						rnextx = rnextx + dx[3];
						if(array[rnextx][rnexty]=='.') { // 이동
							array[rnextx-dx[3]][rnexty] = '.';
							array[rnextx][rnexty] = 'R';						
						}
						else if(array[rnextx][rnexty]=='O') { // 구멍 빠짐
							array[rnextx-dx[3]][rnexty] = '.';
							rnextx = -1;
							rnexty = -1;
							break;
						}
						else {
							rnextx = rnextx - dx[3];
							break;
						}
					}						
				}
				else {
					while(1) {
						rnextx = rnextx + dx[3];
						if(array[rnextx][rnexty]=='.') { // 이동
							array[rnextx-dx[3]][rnexty] = '.';
							array[rnextx][rnexty] = 'R';						
						}
						else if(array[rnextx][rnexty]=='O') { // 구멍 빠짐
							array[rnextx-dx[3]][rnexty] = '.';
							rnextx = -1;
							rnexty = -1;
							break;
						}
						else {
							rnextx = rnextx - dx[3];
							break;
						}
					}	

					while(1) {
						bnextx = bnextx + dx[3];
						if(array[bnextx][bnexty]=='.') { // 이동
							array[bnextx-dx[3]][bnexty] = '.';
							array[bnextx][bnexty] = 'B';
						}
						else if(array[bnextx][bnexty]=='O') { // 구멍 빠짐
							array[bnextx-dx[3]][bnexty] = '.';
							bnextx = -1;
							bnexty = -1;
							break;
						}
						else {
							bnextx = bnextx - dx[3];
							break;
						}
					}										
				}

				if(rnextx==-1 && rnexty==-1 && bnextx!=-1) {
					return count;
				}

				//if((bnextx!=-1)&&(bvisit[bnextx][bnexty]==0 || rvisit[rnextx][rnexty] == 0 || bvisit[bnextx][bnexty]!=rvisit[rnextx][rnexty]))  {
				if((bnextx!=-1)&&(visit[rnextx][rnexty][bnextx][bnexty]==0)) {

					printf("> 아래쪽 이동 큐 삽입 \n");
					for(i=0;i<N;i++) {
						for(j=0;j<M;j++) {
							printf("%c ",array[i][j]);
						}
						printf("\n");	
					}			
					visit[rnextx][rnexty][bnextx][bnexty] = count;
					//bvisit[bnextx][bnexty] = count;	
					//rvisit[rnextx][rnexty] = count;	
					bqueuex[rear] = bnextx;
					bqueuey[rear] = bnexty;
					rqueuex[rear] = rnextx;
					rqueuey[rear] = rnexty;
					rear++;									
				}

				if(bnextx!=-1) array[bnextx][bnexty]='.';
				if(rnextx!=-1) array[rnextx][rnexty]='.';
				
			}
		}
			count++;
			if(count > 10) {
				return -1;
			}
	}
	return -1;
}

int main(void) {
	int i,j;
	int result;
	scanf("%d %d",&N,&M);
	for(i=0;i<N;i++) {
		scanf("%s",array[i]);
		for(j=0;j<M;j++) {
			if(array[i][j]=='R') {
				redx = i;
				redy = j;
			}
			else if(array[i][j]=='B') {
				bluex = i;
				bluey = j;

			}
		}
	}

	result = BFS();

	printf("%d \n",result);

	return 0;
}