#include<iostream>
//#include<fstream>
#include<stdlib.h>
using namespace std;

int N, K,cnt_num=0,cnt_num2=0;

int queue[100000000]={0}, queue_len=0,queue_head,queue_end,visted[100002]={0},ret=0;

int bfs()
{
	int new_N1,new_N2,new_N3,dequeued_N,tmp;

	if(N==K)
	{
		cnt_num2=1;
		return 0;
	}
	//cout<<"bfs"<<endl;
	while(1)
	{
		//cout << "cnt_num";
		cnt_num++;

		//cout<<visted[100]<<endl;
		//cin>>tmp;

		for(int i=queue_head;i<queue_end;i++)
		{
			//cout << "dequeued_N";
			dequeued_N = queue[i];
			new_N1 = dequeued_N-1;
			new_N2 = dequeued_N+1;
			new_N3 = dequeued_N*2;

			//cout<<new_N1<<" "<<new_N2<<" "<<new_N3<<" ";

			if((new_N1 == K)||(new_N2 == K)||(new_N3 == K))
			{
				if(new_N1 == K)
				{
					cnt_num2++;
				}
				if(new_N2 == K)
				{
					cnt_num2++;
				}
				if(new_N3 == K)
				{
					cnt_num2++;
				}
				ret=1;
			}
			else
			{
				if((new_N1<=100000)&&(new_N1>=0))
				{
					if((visted[new_N1] == 0)||(visted[new_N1] == cnt_num))
					{
						queue[queue_len]=new_N1;
						queue_len++;
						visted[new_N1] = cnt_num;
						//cout << "new_N1";
					}
				}
				if((new_N2<=100000)&&(new_N2>=0))
				{
					if((visted[new_N2] == 0)||(visted[new_N2] == cnt_num))
					{
						queue[queue_len]=new_N2;
						queue_len++;
						visted[new_N2] =cnt_num;
						//cout << "new_N2";
					}
				}
				if((new_N3<=100000)&&(new_N3>=0))
				{
					if((visted[new_N3] == 0)||(visted[new_N3] == cnt_num))
					{
						queue[queue_len]=new_N3;
						queue_len++;
						visted[new_N3] =cnt_num;
						//cout << "new_N3";
					}
				}
			}
		}
		if(ret)
		{
			return cnt_num;
		}
		queue_head = queue_end;
		queue_end = queue_len;
		//cout<<"while1"<<endl;
	}
}

int main()
{
	cin>>N;
	cin>>K;

	queue[queue_len]=N;
	visted[N]=1;
	queue_len++;
	queue_head=0;
	queue_end=1;

	cout<<bfs()<<endl;
	cout<<cnt_num2;

	return 0;
}