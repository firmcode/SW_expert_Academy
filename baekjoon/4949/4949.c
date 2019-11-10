#include <iostream>

#include <stdio.h>
#include <string.h>
using namespace std;


char array[105];
char stack[105];
int top;

int stackoper(char *array) {
	int i,len;
	char pop;
	len = strlen(array);
	for(i=0;i<len;i++) {
		switch(array[i]) {
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
	int result=0,len;
	
	while(1) {
		scanf("%[^\n]",array);
		len = strlen(array);
		if(len==1 && array[0]=='.') break;
		result = stackoper(array);
		if(array[len-1]=='.') {
			if(result == 0) cout<<"yes"<<endl;
			else cout<<"no"<<endl;
			result = 0;
			top = 0;			
		}
		fflush(stdin);
	}
	return 0;
}