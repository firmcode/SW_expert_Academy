#include <stdio.h>
int array[105][105];
int visited[105][105];

int BFS(int currentx,int currenty) {
	int i,j;
	int distance = 0;
	for(i=0;i<100;i++) {
		for(j=0;j<100;j++) {
			visited[i][j] = 0;
		}
	}

	while(currentx < 99) {
		visited[currentx][currenty] = 1;
		if(currenty+1<100 && array[currentx][currenty+1]==1 && visited[currentx][currenty+1]==0) {
			currenty = currenty + 1;
			distance++;
		}
		else if(currenty-1>=0 && array[currentx][currenty-1]==1 && visited[currentx][currenty-1]==0) {
			currenty = currenty - 1;
			distance++;
		}
		else if (array[currentx+1][currenty]==1){
			currentx = currentx + 1;
			distance++;
		}
		else
		{
			printf("error!!!\n");

			for(i=0;i<100;i++) {
				for(j=0;j<100;j++) {
					printf("%d",visited[i][j]);
				}
				printf("\n");
			}
			break;
		}
	}
	return distance;
}

int main(void) {
	int test_case,t;
	int i,j;
	int min,result,ans=0;
	for(test_case=1;test_case<=10;test_case++) {
		min = 10005;
		for(i=0;i<100;i++) {
			for(j=0;j<100;j++) {
				scanf("%d",&array[i][j]);
			}
		}
		for(j=0;j<100;j++) {
			if(array[0][j] == 1) {
				result = BFS(0,j);
				if(result < min) {
					min = result;
					ans = j;
				}
			}
		}
		printf("#%d %d %d\n",test_case,ans,min);
		//printf("#%d %d \n",test_case,ans);
	}
	return 0;
}