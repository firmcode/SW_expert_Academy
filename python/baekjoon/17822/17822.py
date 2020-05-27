import sys
dxdy = [[0,1],[0,-1],[1,0],[-1,0]]
def remove_cmp():
	#check_change = [0 for col in range(N)]
	check_change = 0
	new_matrix = [[] for col in range(N)]
	for idy in range(N):
		new_matrix[idy] = matrix[idy][:]


	for idy in range(N):
		for idx in range(M):
			now_val = matrix[idy][idx]
			if now_val == 0 :
				continue

			for get_dir in dxdy:
				new_y = idy + get_dir[0]
				new_x = idx + get_dir[1]
				if new_x < 0:
					new_x = (-1)%M
				elif new_x >= M:
					new_x = 0

				if new_x < 0 or new_y < 0 or new_y >= N or new_x >= M:
					continue

				new_val = new_matrix[new_y][new_x]
				if now_val == new_val:
					matrix[idy][idx] = 0
					check_change = 1

	#for get_check in check_change:
	val_cnt = 0
	get_sum = 0
	if check_change == 0:
		for get_matrix in matrix:
			for get_val in get_matrix:
				if get_val != 0:
					val_cnt = val_cnt + 1
					get_sum = get_sum + get_val
		if val_cnt == 0:
			return
		now_avg = get_sum / val_cnt

		for idy in range(N):
			for idx in range(M):
				now_val = matrix[idy][idx]
				if now_val != 0 :
					if now_val > now_avg :
						matrix[idy][idx] = now_val - 1
					elif now_val < now_avg :
						matrix[idy][idx] = now_val + 1

def rot(x,d,k):
	if d == 0:
		for idx, get_matrix in enumerate(matrix):
			if (idx +1)%x !=0:
				continue
			for get_k in range(k):
				get_matrix = [get_matrix[-1]] + get_matrix[:-1]
				matrix[idx] = get_matrix

	elif d == 1:
		for idx, get_matrix in enumerate(matrix):
			if (idx +1)%x !=0:
				continue
			for get_k in range(k):
				get_matrix = get_matrix[1:] + [get_matrix[0]]
				matrix[idx] = get_matrix
	

N,M,T = map(int, sys.stdin.readline().split())

matrix = []

for idx in range(N):
	matrix.append(list(map(int, sys.stdin.readline().split())))

T_matrix = []
for idx in range(T):
	T_matrix.append(list(map(int, sys.stdin.readline().split())))

for get_T_matrix in T_matrix:
	rot(get_T_matrix[0],get_T_matrix[1],get_T_matrix[2])
	remove_cmp()

total_sum = 0
for get_matrix in matrix:
	now_sum = sum(get_matrix)
	total_sum = total_sum + now_sum

print(total_sum)
#print(matrix)

