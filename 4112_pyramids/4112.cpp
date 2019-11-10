#include<iostream>
using namespace std;

int pyramid[150][150]={0};

int a,b,present_T;
int bfs_queue_x[10002],bfs_queue_y[10002],queue_top=0,queue_bottom=0;
int visted_list[10002];

int dx[] = { -1,0, +1, 0,-1,1};
int dy[] = { 0, +1,0,-1,-1,1};
int found_x,found_y;
int dequeue_x,dequeue_y;

int enqueue(int x, int y)
{
	bfs_queue_x[queue_top]=x;
	bfs_queue_y[queue_top]=y;
	queue_top++;
	return 0;
}
int dequeue()
{
	dequeue_x = bfs_queue_x[queue_bottom];
	dequeue_y = bfs_queue_y[queue_bottom];
	queue_bottom++;
	return 0;
}

int find_index(int find_num)
{

	int i,j;
	for(i=0;i<find_num+1;i++)
	{
		if(find_num==1)
		{
			found_y=0;
			found_x=0;
			return 0;
		}
		if(find_num<(((i*(i+1))/2)+1))
		{
			i=i-1;
			found_y=i;
			found_x = find_num-(((i*(i+1))/2)+1);
			//cout<<"find_num"<<find_num<<" "<<found_x<<" "<<found_y<<endl;
			return 0;
		}
	}

	return -1;

}
int clear_queue()
{
	int i = queue_top;
	//cout<<"queue_top : "<<queue_top<<endl;
	for(;i>=0;i--)
	{
		bfs_queue_x[i]=0;
		bfs_queue_y[i]=0;
	}

	queue_top=0;
	queue_bottom=0;
	return 0;
}

int bfs()
{
	int a_x,b_x,a_y,b_y;
	int cnt=0,present_top,enqueue_x,enqueue_y,present_num;
	queue_top=0,queue_bottom=0;

	if(a==b)
	{
		return 0;
	}

	find_index(a);
	a_x=found_x;
	a_y=found_y;
	enqueue(a_x,a_y);

	while(1)
	{
		present_top=queue_top;
		while(present_top!=queue_bottom)
		{
			dequeue();
			//cout<<"dequeue"<<dequeue_x<<" "<<dequeue_y<<endl;
			for(int i=0;i<6;i++)
			{
				enqueue_x = dequeue_x + dx[i];
				enqueue_y = dequeue_y + dy[i];
				if((enqueue_x<0)||(enqueue_y<0)||(pyramid[enqueue_x][enqueue_y]==0))
				{
					///cout<<"not enqueue"<<enqueue_x<<" "<<enqueue_y<<" "<<pyramid[enqueue_x][enqueue_y]<<endl;
					continue;
				}


				present_num=(((enqueue_y*(enqueue_y+1))/2)+1) + enqueue_x;
				//cout<<"present_num"<<present_num<<endl;
				if(present_num==b)
				{
					///cout<<"retrun"<<endl;
					cnt++;					
					return cnt;
				}
				else if(visted_list[present_num]!=present_T)
				{
					visted_list[present_num]=present_T;
					enqueue(enqueue_x,enqueue_y);
					//cout<<"enqueue"<<queue_top<<endl;
				}
			}
		}
		cnt++;	
		
	}
	return -1;


}


int main()
{
	int i,j,num=1,T,output;

	for(i=0;num<10000;i++)
	{
		for(j=0;j<=i;j++)
		{
			pyramid[j][i] = num;
			num++;

			if(num>10000)
			{
				break;
			}
		}
		//cout<<endl;
	}

	cin>>T;
	for(present_T=1;present_T<=T;present_T++)
	{	
		cin>>a>>b;
		//cout<<a<<" "<<b<<endl;

		output=bfs();

		cout<<"#"<<present_T<<" "<<output<<endl;
		clear_queue();

	}

	return 0;
}