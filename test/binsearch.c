#include <stdio.h>
int binarysearch(int *array, int first, int last, int num) {
	if(first > last) {
	//	printf("0 \n");
		return 0;
	}
	int pivot = (first + last) /2;
	if(num == array[pivot]) {
	//	printf("1 \n");
		return 1;
	}
	else if(num > array[pivot]) 
	{
		return binarysearch(array,pivot+1,last,num);
	}
	else 
	{
		return binarysearch(array,first,pivot-1,num);
	}

}

int main(void) {
	int array[10] = {0,1,2,3,4,5,6,7,8,9};
	binarysearch(array,0,9,15);
	printf("%d \n",binarysearch(array,0,9,15));
	return 0;
}