#include<iostream>
//#include<fstream>
#include<stdlib.h>
using namespace std;


int index1, head_index,head_max=1000,curr_index,found_head_index;

typedef struct NODE{
	int diff_weight;
	int sample_name;
	struct NODE* next;
} node;

node* head = (node*)malloc(sizeof(node)*1000);
node* found_node;
void print_nodes()
{
	node* temp;
	for(int head_i=0;head_i<head_max;head_i++)
	{
		temp=&head[head_i];
		if(temp->next==NULL)
		{
			break;
		}
		while(temp!=NULL)
		{
			cout<<"print sample_name"<<(temp->sample_name)<<" "<<(temp->diff_weight)<<endl;
			temp=temp->next;
		}
		//return 0;
	}
}


void add_node(int sample_id,int diff_weight)
{
	//cout<<"insert sample_id"<<sample_id<<endl;
	node* newnode =(node*)malloc(sizeof(node));
	newnode->sample_name=sample_id;
	newnode->diff_weight=diff_weight;
	newnode->next = found_node->next;///found node
	found_node->next=newnode;
}
int search_node(int sample_id)
{
	node* temp;
	for(int head_i=0;head_i<head_max;head_i++)
	{
		temp=&head[head_i];
		temp=head;
		index1=0;
		if(temp->next==NULL)
		{
			break;
		}
		while(temp!=NULL)
		{
			if((temp->sample_name)==sample_id)
			{
				found_node=temp;
				found_head_index=head_i;
				return 1;
			}
			index1=index1+1;
			temp=temp->next;
		}
	}
	return 0;
}
int calc_diff(node* temp1, node* temp2)
{	
	node* next_node;
	int sum_diff=0;
	next_node=temp1;
	while((next_node->sample_name)!=(temp2->sample_name))
	{	
		sum_diff = sum_diff + next_node->diff_weight;
		next_node=next_node->next;
	}
	return sum_diff;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int test_size,sample_n, works_m;
	int sample1,sample2, diff_weight;
	int sample1_index, sample2_index;
	int calced_diff,calced_diff_pre;
	int temp1_head_index,temp2_head_index;
	node* temp1;
	node* temp2;
	char select_work;



	//ifstream in("sample_input.txt");
	//in.is_open();

	cin>>test_size;
	for(int i=0;i<test_size;i++)//
	{
		for(int head_i=0;head_i<head_max;head_i++)
		{
			head[head_i].next=NULL;
		}
		cout<<"#"<<i+1<<" ";

		cin>>sample_n;
		cin>>works_m;
		for(int j=0;j<works_m;j++)
		{
			//cout<<"works_m: "<<j<<endl;
			print_nodes();
			cin>>select_work;
			if(select_work=='!')
			{
				cin>>sample1;
				cin>>sample2;
				cin>>diff_weight;

				if(search_node(sample1))
				{
					//cout<<"found!!"<<sample1<<endl;
					temp1=found_node->next;
					temp2=found_node;
					while(1)
					{
						if(temp1==NULL)
						{
							found_node = temp2;
							add_node(sample2,0);
							found_node->diff_weight=diff_weight;
							//cout<<"calced_diff!!"<<calced_diff<<endl;
							break;
						}
						calced_diff=calc_diff(found_node,temp1);
						if(diff_weight<calced_diff)
						{	
							calced_diff_pre=calc_diff(found_node,temp2);
							found_node=temp1;
							add_node(sample2,calced_diff-calced_diff_pre);
							temp1->diff_weight = diff_weight - calced_diff_pre;
							break;
						}
						temp2=temp1;
						temp1=temp1->next;
					}
				}
				else if(search_node(sample2))
				{

					temp1 = &head[found_head_index];
					temp2 = &head[found_head_index];
					//temp2=found_node;
					while(1)
					{
						calced_diff=calc_diff(temp1,found_node);
						if(diff_weight>calced_diff)
						{	
							found_node=temp2;
							add_node(sample1,diff_weight-calced_diff);
							temp2->diff_weight = temp2->diff_weight - (diff_weight-calced_diff);
							head[found_head_index].diff_weight=0;
							break;
						}
						temp2=temp1;
						temp1=temp1->next;
					}
				}
				else
				{
					found_node=&head[curr_index];
					add_node(sample1,diff_weight);
					found_node=head[curr_index].next;
					add_node(sample2,0);
				}

				//add_node(sample1,diff_weight);
				//cout<<sample1<<sample2<<diff_weight<<endl;


			}
			else if(select_work=='?')
			{
				cin>>sample1;
				cin>>sample2;
				if(search_node(sample1))
				{
					temp1=found_node;
					temp1_head_index = found_head_index;
					sample1_index=index1;
					if(search_node(sample2))
					{	
						temp2=found_node;
						temp2_head_index = found_head_index;
						sample2_index=index1;
						if(temp2_head_index!=temp1_head_index)
						{
							cout<<"UNKNOWN";
						}
						else if(sample1_index<sample2_index)
						{
							calced_diff=calc_diff(temp1,temp2);
							//cout<<"diff : "<<calced_diff;
							cout<<calced_diff;
						}
						else
						{
							calced_diff=calc_diff(temp2,temp1);
							//cout<<"diff : -"<<calced_diff;	
							cout<<"-"<<calced_diff;
						}
						
					}
					else
					{
						cout<<"UNKNOWN";
					}
				}
				else
				{
					cout<<"UNKNOWN";
				}
				cout<<" ";
			}
			else
			{
				cout<<"Error!!!"<<endl;
			}
		}
		cout<<endl;
	}
	return 0;
}