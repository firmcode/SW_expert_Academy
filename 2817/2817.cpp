#include<iostream>
using namespace std;
int input_list[21];
int anscnt=0,N,K;


int dfs(int nowsum,int now_idx)
{

	if(nowsum == K)
	{
		anscnt=anscnt+1;
		return 0;

	}
	if(now_idx==N)
	{	
		return 0;
	}
	dfs(nowsum + input_list[now_idx],now_idx+1);
	dfs(nowsum,now_idx+1);

}

int main()
{
	int T,tmp;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		anscnt=0;
		cin>>N;
		cin>>K;

		for(int j=0;j<N;j++)
		{
			cin>>tmp;
			input_list[j]=tmp;
		}

		dfs(0,0);
		cout<<"#"<<i<<" "<<anscnt<<endl;

	}
	return 0;
}