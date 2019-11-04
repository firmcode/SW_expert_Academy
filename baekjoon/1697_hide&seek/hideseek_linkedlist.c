#include<iostream>
//#include<fstream>
#include<stdlib.h>
using namespace std;

int N, K,cnt_num=0;

typedef struct NODE{
	int now_N;
	struct NODE* next;
} node;

int visted[100000], visted_len=0;

node* head = (node*)malloc(sizeof(node));

int bfs()
{
	int new_N1,new_N2,new_N3,dequeued_N;

	if(N==K)
	{
		return 0;
	}
	//cout<<"bfs"<<endl;
	while(head->next!=NULL)
	{
		//cout<<"while1"<<endl;
		node* now_node = head;
		node* tmp;

		node* new_head = (node*)malloc(sizeof(node));
		new_head->next=NULL;

		cnt_num = cnt_num +1;

		while(now_node->next != NULL)
		{
			now_node = now_node->next;
			dequeued_N = now_node->now_N;

			new_N1 = dequeued_N-1;
			new_N2 = dequeued_N+1;
			new_N3 = dequeued_N*2;
			//cout<<new_N1<<" "<<new_N2<<" "<<new_N3<<" ";
			if((dequeued_N ==K)||(new_N1 == K)||(new_N2 == K)||(new_N3 == K))
			{
				return cnt_num;
			}
			else
			{
				tmp = new_head;
				while(tmp->next != NULL)
				{
					tmp = tmp->next;
				}

				for(int i=0;i<visted_len;i++)
				{
					if(visted[i] == new_N1)
					{
						new_N1 = -1;
					}
					if(visted[i] == new_N2)
					{
						new_N2 = -1;
					}
					if(visted[i] == new_N3)
					{
						new_N3 = -1;
					}
				}
				if(new_N1 != -1)
				{
					visted[visted_len]=new_N1;
					node* newnode1 =(node*)malloc(sizeof(node));
					newnode1->now_N = new_N1;
					tmp->next = newnode1;
					newnode1->next=NULL;
					tmp = newnode1;
				}
				if(new_N2 != -1)
				{
					node* newnode1 =(node*)malloc(sizeof(node));
					newnode1->now_N = new_N2;
					tmp->next = newnode1;
					newnode1->next=NULL;
					tmp = newnode1;
				}
				if(new_N3 != -1)
				{
					node* newnode1 =(node*)malloc(sizeof(node));
					newnode1->now_N = new_N3;
					tmp->next = newnode1;
					newnode1->next=NULL;
					tmp = newnode1;
				}

			}
		}
		head=new_head;
		//cout<<"while1"<<endl;
	}
}

int main()
{
	cin>>N;
	cin>>K;


	node* newnode =(node*)malloc(sizeof(node));

	head->next = newnode;
	newnode->now_N = N;
	newnode->next = NULL;

	visted[visted_len]=N;
	visted_len++;

	cout<<bfs();

	return 0;
}