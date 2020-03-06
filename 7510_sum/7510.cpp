#include<iostream>
using namespace std;
int T,Num;
int cnt=0;

int main()
{
	//printf("test: %d",)
	int min_n,i,n,b;
	unsigned formula,un,ub;

	//n=1;
	//un=n;
	//printf("un : %d\n",un);


	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cnt = 0;
		cin>>Num;
		//get min n
		for(i=0;i<Num;i++)
		{
			if(Num<(i*(i+1)/2))
			{
				break;
			}
		}
		min_n = i-1;
		//cout<<"min_n : "<<min_n<<endl;
		for(n=Num/2+1;n>=min_n-1;n--)
		{
			un=n;
			for(b=n-1;b>=0;b--)
			{
				ub=b;
				//cout<<"n, b : "<<n<<" "<<b<<endl;
				formula=((un*(un+1)/2) - ub*(ub+1)/2);
				if(formula== Num)
				{
					//cout<<"cnt++"<<endl;
					cnt++;
				}
				else if(formula > Num)
				{
					break;
				}
			}
		}
		if(Num>2)
		{
			cnt++;
		}

		cout<<"#"<<t<<" "<<cnt<<endl;

		//(b*(b+1)/2 - (n*(n+1)/2)=Num;
	}
	return 0;
}
