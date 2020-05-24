
#include <stdio.h>
int array[8] = {1,2,3,4,5,6,7,8};
int result[8],select[8];
int N=4,MAX=8;
 
void combination(int count,int idx) {
	int i;
	if(count == N) {
		for(i=0;i<MAX;i++) printf("%d ",select[i]);
		printf("\n");
		return;		
	}
	for(i=idx;i<MAX;i++) {
		if(select[i] == 0) {
			select[i] = 1;
			result[count] = array[i];
			combination(count+1,i+1);
			select[i] = 0;
		}		
	}
}
 
int main(void) {
	combination(0,0);
}
