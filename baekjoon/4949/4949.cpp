#include <iostream>

#include <stdio.h>
#include <string.h>
using namespace std;


char array_list[105];
char stack[105];
int top;

int stackoper(char *array_list) {
	int i,len;
	char pop;
	len = strlen(array_list);
	for(i=0;i<len;i++) {
		switch(array_list[i]) {
			case '(':
				stack[top++] = '(';
				break;
			case ')':
				if(top==0) return -1;
				pop = stack[--top];
				if(pop == '[') return -1;
				break;
			case '[':
				stack[top++] = '[';
				break;
			case ']':
				if(top==0) return -1;
				pop = stack[--top];
				if(pop == '(') return -1;
				break;
		}
	}
	if(top == 0)return 0;
	else return -1;
}

int main(void) {
	int result=0,len=0;
	char ch;
	
	while(1) {
		scanf("%[^\n]",array_list);
		/*
		len=0;
		while(ch!='\n')
		{
			ch = getchar(stdin);
			array_list[len]=ch;
			len++;
			cout<<ch<<endl;
		}
		fflush(stdin);
		*/
		fflush(stdin);
		len = strlen(array_list);
		if(len==1 && array_list[0]=='.') break;
		result = stackoper(array_list);
		if(array_list[len-1]=='.') {
			if(result == 0) 
			{
				cout<<"yes"<<endl;
			}
			else
			{
				cout<<"no"<<endl;
			}
			result = 0;
			top = 0;			
		}
	}
	return 0;
}