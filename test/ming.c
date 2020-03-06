#include <stdio.h>
int array[1000005];

int makeNum(int N) {
	if((N>1000005)||(N<0))
	{
		printf("Error //// N = %d",N);
	}
	printf("%d\n",N);

	if(N == 1) return 1;
	if(N == 2) return 2;
	if(array[N] != 0) return array[N];
	return array[N] = (makeNum(N-1) + makeNum(N-2))%15746;
}

int main(void) {
	int N,result;
	int i;
	scanf("%d",&N);
	result = makeNum(N);
	printf("%d \n",result);
	return 0;
}

