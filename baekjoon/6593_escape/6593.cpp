#include<stdio.h>
#include<iostream>

using namespace std;

int L,R,C;
char building_arry[30][30][30];
int visited_arry[30][30][30];
int queue_x[27000],queue_y[27000],queue_z[27000];
int queue_top=0,queue_index=0;
int cnt=0;

int dx[6] = {0,0,1,-1,0,0};
int dy[6] = {1,-1,0,0,0,0};
int dz[6] = {0,0,0,0,-1,1};

int bfs()
{
	int present_x,present_y,present_z;
	int next_x,next_y,next_z;
	int qsize;

	while(queue_index!=queue_top)
	{	
		qsize = queue_top - queue_index;
		for(int qsizei=0;qsizei<qsize;qsizei++)
		{
			//dequeue
			present_x = queue_x[queue_index];
			present_y = queue_y[queue_index];
			present_z = queue_z[queue_index];
			queue_index++;
			

			if(building_arry[present_z][present_y][present_x]=='E')
			{
				//return visited_arry[present_z][present_y][present_x];
				return cnt;
			}

			for(int i=0;i<6;i++)
			{
				next_z = present_z + dz[i];
				next_y = present_y + dy[i];
				next_x = present_x + dx[i];

				if((building_arry[next_z][next_y][next_x]!='#')&&(visited_arry[next_z][next_y][next_x]==0)&&(next_z>=0)&&(next_y>=0)&&(next_x>=0)&&(next_z<L)&&(next_y<R)&&(next_x<C))
				{
					//inqueue
					visited_arry[next_z][next_y][next_x]=1;
					queue_x[queue_top]=next_x;
					queue_y[queue_top]=next_y;
					queue_z[queue_top]=next_z;
					queue_top++;
				}
			}
		}
		cnt++;
	}
	return -1;
}

int main()
{
	int output, start_x, start_y, start_z;
	while(1)
	{
		cin>>L;
		cin>>R;
		cin>>C;

		if((L==0)&&(R==0)&&(C==0))
		{
			break;
		}

		for(int iL=0;iL<L;iL++)
		{
			for(int iR=0;iR<R;iR++)
			{
				for(int iC=0;iC<C;iC++)
				{
					scanf(" %c", &building_arry[iL][iR][iC]);
					if(building_arry[iL][iR][iC]=='S')
					{
						start_x = iC;
						start_y = iR;
						start_z = iL;
					}
				}
			}
		}

		queue_x[0]=start_x;
		queue_y[0]=start_y;
		queue_z[0]=start_z;
		++queue_top;
		visited_arry[start_x][start_y][start_z]=1;

		output=bfs();
		if(output>0)
		{
			printf("Escaped in %d minute(s).\n",output);
		}
		else
		{
			printf("Trapped!\n");		
		}

		//clear
		for(int i=0;i<queue_top;i++)
		{
			queue_x[i]=0;
			queue_y[i]=0;
			queue_z[i]=0;
		}
		cnt=0;
		queue_top=0;
		queue_index=0;
		for(int iL=0;iL<30;iL++)
		{
			for(int iR=0;iR<30;iR++)
			{
				for(int iC=0;iC<30;iC++)
				{
					visited_arry[iL][iR][iC]=0;
				}
			}
		}

	}
	return 0;
}