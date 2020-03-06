#include <stdio.h>
struct node {
	double pos; // 위치
	double weight; // 질량
};
struct node coordinate[15];

int main(void) {
	int T,test_case;
	int N,i,k,count;
	double left,right,mid,sum; // 이진 탐색용

	scanf("%d",&T);
	for(test_case=1;test_case<=T;test_case++) {
		scanf("%d",&N);
		for(i=0;i<N;i++) {
			scanf("%lf ",&coordinate[i].pos);
		}
		for(i=0;i<N;i++) {
			scanf("%lf ",&coordinate[i].weight);
		}
		printf("#%d ",test_case);
		for(k=1;k<N;k++) { // 균형점은 N-1개 존재
			left = coordinate[k-1].pos;
			right = coordinate[k].pos;
			count = 0;

			while(1) {
				count++;
				sum = 0;
				mid = (left + right) / 2.0;

				for(i=0;i<k;i++) { // 왼쪽 자성체들의 합
					sum = sum - (coordinate[i].weight) /((mid - coordinate[i].pos)*(mid - coordinate[i].pos));
				}
				for(i=k;i<N;i++) { // 오른쪽 자성체들의 합
					sum = sum + (coordinate[i].weight) /((coordinate[i].pos - mid)*(coordinate[i].pos - mid));
				}
				//printf("mid : %lf left: %lf right : %lf \n",mid , left, right);
				if(sum == 0) break; // 완벽한 균형점 찾았을 때
				if(sum > 0) right = mid; // 균형점이 더 오른쪽에 있을 때
				else left = mid; // 균형점이 더 왼쪽에 있을 때
				if(count > 50) break; // 스택 오버플로우 방지
			}
			printf("%.10lf ",mid);
		}
		printf("\n");
 	}
	return 0;
}