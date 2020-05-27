import sys
dxdy = [[0,1],[0,-1],[-1,0],[1,0]]

max_val = 0

def sim(now_dir,now_matrix):
	global max_val

	visit_matrix = [[0 for row in range(N)] for col in range(N)]
	
	for idy in range(N):
		for idx in range(N):

			if now_dir ==0:
				now_y = idy
				now_x = (-1 - idx)%N
			elif now_dir ==1:
				now_y = idy
				now_x = idx
			elif now_dir ==2:
				now_y = idy
				now_x = idx
			elif now_dir ==3:
				now_y = (-1 - idy)%N
				now_x = idx

			if now_matrix[now_y][now_x] == 0:
				continue

			while 1:

				new_y = now_y + dxdy[now_dir][0]
				new_x = now_x + dxdy[now_dir][1]

				if new_y >= N or new_x >= N or new_y < 0 or new_x < 0 or visit_matrix[new_y][new_x]==1:
					break
				if now_matrix[now_y][now_x] == now_matrix[new_y][new_x]:
					new_val = now_matrix[new_y][new_x] *2
					now_matrix[new_y][new_x] = new_val
					now_matrix[now_y][now_x] = 0
					visit_matrix[new_y][new_x] = 1
					if max_val < new_val :
						max_val = new_val

					break

				elif now_matrix[new_y][new_x] ==0:
					now_matrix[new_y][new_x] = now_matrix[now_y][now_x]
					now_matrix[now_y][now_x] = 0
				else :
					break
				now_y = new_y
				now_x = new_x
	
	return now_matrix



N = int(sys.stdin.readline())

matrix = []

for ind in range(N):
	col = list(map(int, sys.stdin.readline().split()))
	now_max = max(col)
	if max_val < now_max:
		max_val = now_max
	matrix.append(col)

#for ind in range(N):
dir_cnt = 4

for dir1 in range(dir_cnt):
	cp_matrix1 = [[] for col in range(N)]
	for ind1 in range(N):
		cp_matrix1[ind1] = matrix[ind1][:]
	new_matrix1 = sim(dir1,cp_matrix1)

	for dir2 in range(dir_cnt):
		cp_matrix2 = [[] for col in range(N)]
		for ind1 in range(N):
			cp_matrix2[ind1] = new_matrix1[ind1][:]
		new_matrix2 = sim(dir2,cp_matrix2)

		for dir3 in range(dir_cnt):
			cp_matrix3 = [[] for col in range(N)]
			for ind1 in range(N):
				cp_matrix3[ind1] = new_matrix2[ind1][:]
			new_matrix3 = sim(dir3,cp_matrix3)

			for dir4 in range(dir_cnt):
				cp_matrix4 = [[] for col in range(N)]
				for ind1 in range(N):
					cp_matrix4[ind1] = new_matrix3[ind1][:]
				new_matrix4 = sim(dir4,cp_matrix4)

				for dir5 in range(dir_cnt):
					cp_matrix5 = [[] for col in range(N)]
					for ind1 in range(N):
						cp_matrix5[ind1] = new_matrix4[ind1][:]
					new_matrix5 = sim(dir5,cp_matrix5)

print(max_val)