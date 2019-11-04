#include<iostream>
//#include<fstream>
#include<stdlib.h>
using namespace std;

int N, M;
int maze[1000][1000];
int min_x=100000000;

struct PRE_INDEX{
	int x;
	int y;
} dfs_index;

int dx[] = { -1,0, +1, 0};
int dy[] = { 0, +1,0,-1};

void DFS(int count_x)
{
	int tmp_x,tmp_y;
	
	count_x = count_x +1;
	if((dfs_index.x == N-1)&&(dfs_index.y == M-1))
	{
		if(count_x < min_x)
		{
			min_x = count_x;
		}
	}
	else if(count_x > min_x)
	{
		return;
	}
	else if(min_x <= M+N-1)
	{
		return;
	}
	else
	{
		for(int i=0;i<4;i++)
		{
			if(((dfs_index.x + dx[i])>-1) && ((dfs_index.y + dy[i])>-1)&&((dfs_index.x + dx[i])<N)&&((dfs_index.y + dy[i])<M))
			{
				if((maze[dfs_index.x + dx[i]][dfs_index.y + dy[i]])==1)
				{
					dfs_index.x = dfs_index.x + dx[i];
					dfs_index.y = dfs_index.y + dy[i];
					tmp_x = dfs_index.x;
					tmp_y = dfs_index.y;

					maze[tmp_x][tmp_y] = 2;
					DFS(count_x);
					maze[tmp_x][tmp_y] = 1;
					dfs_index.x = tmp_x - dx[i];
					dfs_index.y = tmp_y - dy[i];
				}
			}
			if(min_x <= M+N-1)
			{	
				return;
			}
		}
	}
}
int main()
{
	int tmp;
	cin>>N;
	cin>>M;

	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
		{
			scanf("%1d",&tmp);

			if(tmp==1)
			{
				maze[i][j]=1;
			}
			else
			{
				maze[i][j]=0;
			}
		}
	}

	dfs_index.x = 0;
	dfs_index.y = 0;
	maze[dfs_index.x][dfs_index.y] = 2;
	DFS(0);
	cout<<min_x;

}