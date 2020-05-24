cnt = 0

def solution(n, m, k):
	answer = -1

	fact(-1,0,0,n, m, k)

	print(cnt)
	answer = (cnt *2) %1000000007
	print(answer)

	return answer


def fact(ski_type,sum1,sum2,n, m, k):
	global cnt
	if sum2 > m:
		return
	if n == 0:
		if (sum1 == 0) and (sum2 ==m):
			cnt = cnt + 1
		return
	for i in range(1,k+1):
		fact(ski_type*(-1),sum1 + (i * ski_type),sum2 + i,n - 1, m, k)


solution(3,8,4)

#solution(2,10,4)


