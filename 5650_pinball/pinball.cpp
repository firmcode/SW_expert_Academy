#include<iostream>
//#include<fstream>
using namespace std;

int t_matrix[102][102],t;
int result_max;
int start_x,start_y,start_cnt;
int dir;

struct info{
	int x;
    int y;
};

int dx[] = { -1, +1, 0, 0 };
int dy[] = { 0, 0, -1, +1 };

int foundx,foundy;

int curr_x,curr_y,curr_score, curr_dir;

int calc_score()
{
	int x, y,flag=0;
	int warmholl;

	while(1)
	{
		curr_x=curr_x+dx[curr_dir];
		curr_y=curr_y+dy[curr_dir];

		if((curr_x<=-1)||(curr_y<=-1)||(curr_x>=t)||(curr_y>=t))
		{

			curr_score=curr_score+1;
			if(curr_dir==0)
			{
				curr_dir=1;
			}
			else if(curr_dir==1)
			{
				curr_dir=0;
			}
			else if(curr_dir==2)
			{
				curr_dir=3;
			}
			else if(curr_dir==3)
			{
				curr_dir=2;
			}
		}
		else if(((curr_x==start_x)&&(curr_y==start_y)&&(start_cnt==0))||(t_matrix[curr_x][curr_y]==-1))
		{
			if(result_max < curr_score)
			{
				result_max=curr_score;
			}
			return 0;
		}
		else if(t_matrix[curr_x][curr_y]!=0)
		{
			if(t_matrix[curr_x][curr_y]==1)
			{
				curr_score=curr_score+1;
				if(curr_dir==0)
				{
					curr_dir=2;
				}
				else if(curr_dir==1)
				{
					curr_dir=0;
				}
				else if(curr_dir==2)
				{
					curr_dir=3;
				}
				else if(curr_dir==3)
				{
					curr_dir=1;
				}
				//0>2
				//1>0
				//2>3
				//3>1
			}
			else if(t_matrix[curr_x][curr_y]==2)
			{	
				curr_score=curr_score+1;
				if(curr_dir==0)
				{
					curr_dir=3;
				}
				else if(curr_dir==1)
				{
					curr_dir=0;
				}
				else if(curr_dir==2)
				{
					curr_dir=1;
				}
				else if(curr_dir==3)
				{
					curr_dir=2;
				}
				//0>3
				//1>0
				//2>1
				//3>2
			}
			else if(t_matrix[curr_x][curr_y]==3)
			{
				curr_score=curr_score+1;
				if(curr_dir==0)
				{
					curr_dir=1;
				}
				else if(curr_dir==1)
				{
					curr_dir=3;
				}
				else if(curr_dir==2)
				{
					curr_dir=0;
				}
				else if(curr_dir==3)
				{
					curr_dir=2;
				}
				//0>1
				//1>3
				//2>0
				//3>2
			}
			else if(t_matrix[curr_x][curr_y]==4)
			{
				curr_score=curr_score+1;
				if(curr_dir==0)
				{
					curr_dir=1;
				}
				else if(curr_dir==1)
				{
					curr_dir=2;
				}
				else if(curr_dir==2)
				{
					curr_dir=3;
				}
				else if(curr_dir==3)
				{
					curr_dir=0;
				}
				//0>1
				//1>2
				//2>3
				//3>0
			}
			else if(t_matrix[curr_x][curr_y]==5)
			{
				curr_score=curr_score+1;
				if(curr_dir==0)
				{
					curr_dir=1;
				}
				else if(curr_dir==1)
				{
					curr_dir=0;
				}
				else if(curr_dir==2)
				{
					curr_dir=3;
				}
				else if(curr_dir==3)
				{
					curr_dir=2;
				}
				//0>1
				//1>0
				//2>3
				//3>2
			}
			else if((t_matrix[curr_x][curr_y] >=6)&&(t_matrix[curr_x][curr_y] <=10))
			{
				flag=0;
				warmholl = t_matrix[curr_x][curr_y];
				for(int y=0;y<t;y++)
				{
					for(int x=0;x<t;x++)
					{
						if(t_matrix[x][y]==warmholl)
						{
							if((x==curr_x)&&(y==curr_y))
							{
								continue;
							}
							curr_x=x;
							curr_y=y;
							flag=1;
							break;
						}
						
					}
					if(flag==1)
					{
						break;
					}
				}
			}
		}
		start_cnt=0;
	}	
	
	return 0;
}

int main()
{
	int test_size;	
	int matrix_x,matrix_y;

	//ifstream in("sample_input.txt");
	//in.is_open();

	cin>>test_size;
	for(int i=0;i<test_size;i++)
	{
		cin>>t;
		cout<<"#"<<i+1<<" ";
		result_max=0;
		for(int t_y=0;t_y<t;t_y++)
		{
			for(int t_x=0;t_x<t;t_x++)
			{
				cin>>t_matrix[t_x][t_y];
			}
		}
		for(start_y=0;start_y<t;start_y++)
		{
			for(start_x=0;start_x<t;start_x++)
			{
				if(t_matrix[start_x][start_y]==0)
				{
					for(dir=0;dir <4;dir++)
					{

						matrix_x=start_x-dx[dir];
						matrix_y=start_y-dy[dir];
						if((t_matrix[matrix_x][matrix_y]==0)||(matrix_x<=-1)||(matrix_y<=-1))
						{

							matrix_x=start_x+dx[dir];
							matrix_y=start_y+dy[dir];
							if((t_matrix[matrix_x][matrix_y]==0)||(matrix_x<=-1)||(matrix_y<=-1))
							{
								continue;
							}
						}
						curr_x=start_x;
						curr_y=start_y;
						curr_score=0;
						curr_dir=dir;
						start_cnt=1;
						calc_score();
					}
				}
			}
		}
		cout<<result_max<<endl;
	}

	return 0;
}