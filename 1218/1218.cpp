#include<iostream>
//#include<stdlib.h>

using namespace std;

char input_list[1000],T;
int a=0;//()
int b=0;//[]
int c=0;//{}
int d=0;//<>


int main()
{
	int input_size,j;
	char getc;

	for(int i=1;i<=10;i++)
	{
		a=0;
		b=0;
		c=0;
		d=0;
		cin>>input_size;
		cin>>input_list;
		cout<<"#"<<i<<" ";
		//input_size=strlen(input_list);
		for(j=0;j<input_size;j++)
		{
			getc=input_list[j];
			if(getc=='(')
			{
				a++;
			}
			else if(getc==')')
			{
				a--;
			}
			else if(getc=='[')
			{
				b++;
			}
			else if(getc==']')
			{
				b--;
			}
			else if(getc=='{')
			{
				c++;
			}
			else if(getc=='}')
			{
				c--;
			}
			else if(getc=='<')
			{
				d++;
			}
			else if(getc=='>')
			{
				d--;
			}

			if((a<0)||(b<0)||(c<0)||(d<0))
			{
				cout<<"0"<<endl;
				break;
			}
		}
		if((a==0)&&(b==0)&&(c==0)&&(d==0))
		{
			cout<<"1"<<endl;
		}

	}
}