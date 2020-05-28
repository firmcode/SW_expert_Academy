import sys
def check_line(check_matrix):

	#for get_matrix in check_matrix:
	#	print(get_matrix)

	for idx in range(N):
		now_y = 0
		now_x = idx

		next_y = 0
		while next_y < H:	
			#print("now_y,now_x",now_y,now_x)
			if check_matrix[now_y][now_x] == 1:
				next_y = now_y + 1
				next_x = now_x + 1
			elif (now_x-1 >= 0) and check_matrix[now_y][now_x-1] == 1:
				next_y = now_y + 1
				next_x = now_x - 1
			else:
				next_y = now_y + 1
				next_x = now_x
			now_x = next_x
			now_y = next_y


		if idx == now_x :
			continue
		else :
			return -1
	return 1

def rec1(new_matrix,limit_line,now_line,pre_y,pre_x):
	cp_matrix = [[] for row in range(H)]
	for row,get_row in enumerate(new_matrix):
		cp_matrix[row] = get_row[:]

	for idy in range(pre_y,H):
		for idx in range(N-1):
			if (idy <= pre_y and idx <= pre_x) and (idy !=0 and idx!=0):
				continue
			if new_matrix[idy][idx] == 0:
				left_idx = idx - 1
				right_idx = idx + 1

				bool_line = 0 
				if left_idx < 0 and new_matrix[idy][right_idx]:
					bool_line = 1
				elif new_matrix[idy][left_idx]==0 and new_matrix[idy][right_idx]==0:
					bool_line = 1

				if bool_line == 1 :
					cp_matrix[idy][idx] = 1
					now_line = now_line + 1 
					if now_line >= limit_line :
						if check_line(cp_matrix) ==1:
							return 1
					else:
						if rec1(cp_matrix,limit_line,now_line,idy,idx) ==1:
							return 1

					now_line = now_line - 1 
					cp_matrix[idy][idx] = 0
	return -3

N,M,H = map(int, sys.stdin.readline().split())

line_list = []
for idx in range(M):
	a,b = list(map(int, sys.stdin.readline().split()))
	line_list.append([a,b])

matrix = [[0 for col in range(N)] for row in range(H)]

for get_line in line_list:
	idy = get_line[0]
	idx = get_line[1]
	matrix[idy-1][idx-1]=1

if check_line(matrix) == 1 :
	print(0)

else :
	output = -1
	for idx in range(1,4):
		if rec1(matrix,idx,0,0,0) != -3:
			output = idx
			break
	print(output)



#print(rec1(matrix,1,0))