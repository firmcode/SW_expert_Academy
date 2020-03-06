#include<iostream>
using namespace std;
int T,t, input_list[101][101],list_size;
int bfs_queue_x[100000],bfs_queue_y[100000],top_queue,bot_queue;
int bfs_queue_dist[100000];
int dist_list[101][101];
int dx[]={-1,0,1,0};
int dy[]={0,-1,0,1};
int time_sum;

int bfs()
{
	int present_x, present_y,next_x,next_y,new_dist,present_dist;
	int find_min=999999;
	while(top_queue!=bot_queue)
	{
		//dequeue

		present_x = bfs_queue_x[bot_queue];
		present_y = bfs_queue_y[bot_queue];
		present_dist = bfs_queue_dist[bot_queue];
		bot_queue++;
		//cout<<"dequeue x y"<<present_x<<" "<<present_y<<endl;

		if((present_dist > dist_list[present_x][present_y])&&(present_dist<find_min))
		{
			continue;
		}
		if((present_x == list_size-1)&&(present_y == list_size-1))
		{
			//cout<<"return"<<endl;
			find_min=present_dist;
			//return dist_list[list_size-1][list_size-1];
		}

		//enqueue
		for(int i=0;i<4;i++)
		{
			next_x = present_x+dx[i];
			next_y = present_y+dy[i];
			//cout<<"n_x,n_y new_dist : "<<next_x<<" "<<next_y<<" "<<new_dist<<endl;
			if((next_x>=0)&&(next_y>=0)&&(next_x<list_size)&&(next_y<list_size))
			{
				new_dist=dist_list[present_x][present_y]+input_list[next_x][next_y];
				if(dist_list[next_x][next_y] > new_dist)
				{
					//cout<<"enqueue n_x,n_y new_dist : "<<next_x<<" "<<next_y<<" "<<new_dist<<endl;

					dist_list[next_x][next_y] = new_dist;

					bfs_queue_x[top_queue] = next_x;
					bfs_queue_y[top_queue] = next_y;
					bfs_queue_dist[top_queue] = new_dist;
					top_queue++;
				}

			}

		}
	}
	return find_min;
}

int main()
{
	int tmp;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		top_queue=0;
		bot_queue=0;

		cin>>list_size;

		for(int i=0;i<list_size;i++)
		{
			for(int j=0;j<list_size;j++)
			{
				scanf("%1d",&tmp);
				input_list[i][j]=tmp;
				dist_list[i][j]=99999999;


			}
		}
		bfs_queue_x[0]=0;
		bfs_queue_y[0]=0;
		bfs_queue_dist[0]=0;
		dist_list[0][0]=0;
		top_queue++;



		cout<<"#"<<t<<" "<<bfs()<<endl;

	}

}