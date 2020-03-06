#include<iostream>
using namespace std;


char input_list[21][21];
int visited_list[21][21][16];
int visited_list_dir[21][21][5];
int point_x,point_y;
int R,C;
int memory_int;
int veri;
int dx[]={-1,0,1,0};
int dy[]={0,-1,0,+1};
int present_dir;
int t;
int dfs()
{
	char get_current_val;
	int point_x_tmp,point_y_tmp;
	int int_tmp;


	//cout<<"get_current_val: "<<get_current_val<<endl;
	//cout<<"point_y ,x :"<<point_y<<" "<<point_x<<endl;
	//cout<<"memory_int : "<<memory_int<<endl;


	get_current_val=input_list[point_y][point_x];

	if((visited_list[point_y][point_x][memory_int]==1)&&(visited_list_dir[point_y][point_x][present_dir]==1))
	{
		return 0;
	}
	else
	{
		visited_list[point_y][point_x][memory_int]=1;
		visited_list_dir[point_y][point_x][present_dir]=1;
	}

	if(get_current_val=='@')
	{
		veri=1;
		return 1;
	}
	else if(get_current_val=='<')
	{
		present_dir=0;
	}
	else if(get_current_val=='>')
	{
		present_dir=2;
	}
	else if(get_current_val=='^')
	{
		present_dir=1;
	}
	else if(get_current_val=='v')
	{
		present_dir=3;
	}
	else if(get_current_val=='_')
	{
		if(memory_int==0)
		{
			present_dir=2;
		}
		else
		{
			present_dir=0;
		}
	}
	else if(get_current_val=='|')
	{
		if(memory_int==0)
		{
			present_dir=3;
		}
		else
		{
			present_dir=1;
		}
	}
	else if(get_current_val=='?')
	{
		point_x_tmp=point_x;
		point_y_tmp=point_y;
		for(int dir=0;dir<4;dir++)
		{	
			present_dir=dir;

			point_x=(point_x_tmp+dx[present_dir]);
			point_y=(point_y_tmp+dy[present_dir]);

			if(point_x<0)
			{
				point_x=C-1;
			}
			else if(point_x>(C-1))
			{
				point_x=0;
			}

			if(point_y<0)
			{
				point_y=R-1;
			}
			else if(point_y>(R-1))
			{
				point_y=0;
			}	
			dfs();
		}
		return 0;
		//point_x=point_x_tmp;
		//point_y=point_y_tmp;
	}
	else if(get_current_val=='.')
	{
	}
	else if(get_current_val=='+')
	{
		memory_int = (memory_int+1);
		if(memory_int>=16)
		{
			memory_int=0;
		}
	}
	else if(get_current_val=='-')
	{
		memory_int = (memory_int-1);
		if(memory_int<0)
		{
			memory_int=15;
		}
	}
	else
	{
		int_tmp = get_current_val-'0';
		if(int_tmp>9||int_tmp<0)
		{
			cout<<"Error : "<<int_tmp<<endl;
			cout<<"R,C : "<<R<<C<<endl;
			cout<<"point_y ,x :"<<point_y<<" "<<point_x<<endl;

		}
		//cout<<"int_tmp : "<<int_tmp<<endl;
		memory_int=int_tmp;
	}

	point_x=(point_x+dx[present_dir]);
	point_y=(point_y+dy[present_dir]);
	if(point_x<0)
	{
		point_x=C-1;
	}
	else if(point_x>(C-1))
	{
		point_x=0;
	}
	if(point_y<0)
	{
		point_y=R-1;
	}
	else if(point_y>(R-1))
	{
		point_y=0;
	}


	//cout<<"dfscall"<<endl;

	dfs();
	return 0;

}

int main()
{
	int T;
	char tmp;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		point_x=0;
		point_y=0;
		memory_int=0;
		veri=0;

		for(int r=0;r<R;r++)
		{
			for(int c=0;c<C;c++)
			{
				input_list[r][c]=0;
			
				for(int j=0;j<16;j++)
				{
					visited_list[r][c][j]=0;
				}
				for(int j=0;j<4;j++)
				{
					visited_list_dir[r][c][j]=0;
				}
			}
		}

		cin>>R;
		cin>>C;

		for(int r=0;r<R;r++)
		{
			for(int c=0;c<C;c++)
			{
				scanf(" %c",&tmp);
				input_list[r][c]=tmp;

			}
		}
		present_dir=2;
		dfs();
		if(veri==1)
		{
			cout<<"#"<<t<<" YES"<<endl;
		}
		else
		{
			cout<<"#"<<t<<" NO"<<endl;
		}
	}


	return 0;
}