#include<iostream>
//#include<fstream>
#include<stdlib.h>
using namespace std;


int N, P[1000];
int main()
{
	int pre_N,min,tmp,sum=0,save_i,pre_SUM=0;
	cin>>N;
	for(int i=0;i<N;i++)
	{
		cin>>P[i];
		//cout<<P[i];
	}

	pre_N=N;
	//find min
	for(int order_i = 0;order_i<N;order_i++)
	{
		min = P[0];
		for(int i=0;i<pre_N;i++)
		{
			if(min>=P[i])
			{
				min = P[i];
				save_i = i;
			}
		}
		//tmp=P[save_i];
		P[save_i]=P[pre_N-1];
		pre_N=pre_N-1;

		//cout<<min<<"+"<<sum<<endl;
		pre_SUM = pre_SUM + min;
		sum = sum + pre_SUM;
	}
	cout<<sum;


	return 0;
}