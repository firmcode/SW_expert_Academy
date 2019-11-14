#include<iostream>
#include<stdio.h>
using namespace std;
int input_list[100]={1,2,3,4,5},select_N,list_size;
int visted_list[100]={0};
int print_list[100];

int getk(int recursion, int pre_i)
{
	int get_int,j;

	if(recursion<=0)
	{
		return 0;
	}
	for(int i=pre_i;i<list_size;i++)
	{
		get_int=input_list[i];
		if(recursion==select_N)//dequeue
		{
			input_list[i]=-1;
		}

		if((visted_list[get_int]==0)&&(get_int!=-1))
		{
			visted_list[get_int]=1;
			if(recursion==1)
			{
				print_list[select_N-recursion]=get_int;
				for(j=0;j<select_N;j++)
				{
					cout<<print_list[j];
				}
				cout<<endl;
			}
			else
			{
				print_list[select_N-recursion]=get_int;
				
			}
			getk(recursion-1,i);
			visted_list[get_int]=0;
		}
	}
}


int main()
{
	
	int i, k;

	list_size=0;
	while(input_list[list_size]!=0)
	{
		list_size++;
	}

	selcet_N=3;
	getk(selcet_N,0);

	return 0;
}