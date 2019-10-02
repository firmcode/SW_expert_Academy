#include <iostream> 
#include <fstream>
#include <algorithm> 
using namespace std;

int main(void)
{
	int i,j,sum=0;
	int size;
	int buildings[1000]={0,};
	int buildings_ind;
	int center,left1,left2,right1,right2;
	int list[4],max_floor;

	ifstream in("input.txt");
	in.is_open();

	for(int i=0;i<10;i++)
	{
		sum=0;
		in>>size;
		for(int j=0;j < size;j++)
		{
			in>>buildings[j];
		}
		for(int buildings_ind=2;buildings_ind<size;buildings_ind++)
		{
			center = buildings[buildings_ind];
			left1= buildings[buildings_ind-1];
			left2= buildings[buildings_ind-2];
			right1= buildings[buildings_ind+1];
			right2= buildings[buildings_ind+2];
			
			if((center>left1)&&(center>left2)&&(center>right1)&&(center>right2))
			{	
				list[0]=left1;
				list[1]=left2;
				list[2]=right1;
				list[3]=right2;
				max_floor=*max_element(list,list+4);
				sum = sum+(center-max_floor);
			}
		}
		cout<<"#"<<i+1<<" "<<sum<<endl;
	}
	return 0;
}


