#include <iostream> 
//#include <fstream>
#include <vector>
#include <stdlib.h>
#include <algorithm> 
#include <string.h>
using namespace std;

vector<vector<int> > adj;
vector<int> iter_list;
vector<int> route_list;
//vector<vector<int> > node_list;

struct node_list{
    int x;
    int y;
};

int visted[12];
int route[12];
int node_cnt;
int min_val=999999999;
/*
int sum_every_route(int node_cnt,int pre_sum, vector<int> iter_list,int *visted)
{
	int sum=0;
	int i=0;

	vector<int>::iterator iter=iter_list.begin();
	if(node_cnt<=0)
	{
		vector<int>::iterator iter_route=route_list.begin();
		cout<<*iter_route<<" ";
		//for(iter_route=route_list.begin();iter_route!=route_list.end();iter_route++)
		//{
		//	cout<<*iter_route<<" ";
		//}
		cout<<endl;
		
		route_list.pop_back();
		return 0;
	}

	for(iter=iter_list.begin();iter!=iter_list.end();iter++)
	{
		visted[*iter]=1;

		vector<int> new_v(iter_list);
		new_v.erase(new_v.begin()+i);
		i=i+1;

		sum_every_route(node_cnt-1,0,new_v,visted);

		//cout<<endl;
	}
	//sum_every_route(node_cnt-1,pre_sum,iter_list);
	return 0;
}*/

int sum_every_route(int cnt, int sum,int prev)
{
	if(sum > min_val)
	{
		return 0;
	}

	if(cnt<=0)
	{
		//for(int i=0;i<node_cnt;i++)
		//{
		//	cout<<route[i];
		//}
		//cout<<endl;

		sum = sum + adj[prev][node_cnt+1];
		//cout<<adj[prev][6];
		//cout<<"sum"<<sum<<endl;
		if(sum < min_val)
		{
			min_val=sum;
			//cout<<min_val<<endl;
		}
		return 0;
	}

	for(int i=1;i<node_cnt+1;i++)
	{
		if(visted[i]==0)
		{
			//cout<<i;
			visted[i]=1;
			route[node_cnt-cnt]=i;

			//sum = sum+adj[prev][i];
			//cout<<prev<<" "<<i<<" "<<adj[prev][i]<<endl;

			sum_every_route(cnt-1,sum+adj[prev][i],i);

			//sum = sum-adj[prev][i];
			visted[i]=0;
		}
	}

	return 0;
}


int main(void)
{
	int i,j;
	int test_size;


	int x,y;

	//ifstream in("input.txt");
	//cin.is_open();

	struct node_list list[12];

	cin>>test_size;
	for(int i=0;i<test_size;i++)
	{
		min_val=999999999;


		cout<<"#"<<i+1<<" ";
		cin>>node_cnt;
		//node_list=vector<vector<int> >(node_cnt+2, vector<int>(2, 0));
		

		cin>>list[0].x;
		cin>>list[0].y;
		cin>>list[node_cnt+1].x;
		cin>>list[node_cnt+1].y;

		for(int x=1;x<node_cnt+1;x++)
		{
			cin>>list[x].x;
			cin>>list[x].y;
		}

		//cout<<"node_list"<<node_list[0][0]<<endl;
		adj=vector<vector<int> >(node_cnt+2, vector<int>(node_cnt+2, 0));

		for(int x=0;x<node_cnt+2;x++)
		{
			for(int y=0;y<node_cnt+2;y++)
			{
				adj[x][y] = abs(list[x].x-list[y].x)+abs(list[x].y-list[y].y);

				//cout<<x<<" "<<y<<":"<<adj[x][y]<<endl;
				
			}
		}
		iter_list=vector<int>(node_cnt+2);
		for(int x=0;x<node_cnt;x++)
		{
			iter_list[x]=x;
		}

		memset(visted, 0, sizeof(visted));
		sum_every_route(node_cnt,0,0);
		cout<<min_val<<endl;
		//arr[][]
	}
	return 0;
}


