import sys
def test(matrix):
	matrix[0][0] = 0
	for idx in range(N):
		print(matrix[idx])


N,M = map(int, sys.stdin.readline().split())

matrix = [[] for row in range(N)]
poi_xy = []
for idx in range(N):
	matrix[idx] = list(map(int, sys.stdin.readline().split()))
	try :
		poi_x=matrix[idx].index(2)
		poi_xy.append([idx,poi_x])
	except:
		None

for idx in range(N):
	print(matrix[idx])
print("")


tmp = [[] for row in range(N)]

for idx in range(N):
	tmp[idx] = matrix[idx][:]
test(tmp)
print("")


for idx in range(N):
	print(matrix[idx])



