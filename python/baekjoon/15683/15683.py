import sys
'''
cctv_1 = [[[0,1]],[[0,-1]],[[1,0]],[[-1,0]]]
cctv_2 = [[[0,1],[0,-1]],[[1,0],[-1,0]]]
cctv_3 = [[[1,0],[0,1]],[[1,0],[0,-1]],[[-1,0],[0,1]],[[-1,0],[0,-1]]]
cctv_4 = [[[1,0],[-1,0],[0,1]],[[1,0],[-1,0],[0,-1]],[[1,0],[0,1],[0,-1]],[[-1,0],[0,1],[0,-1]]]
cctv_5 = [[[[1,0],[-1,0],[0,1],[0,-1]]]]
'''
cctv_matrix= [[[[0,1]],[[0,-1]],[[1,0]],[[-1,0]]],
[[[0,1],[0,-1]],[[1,0],[-1,0]]],
[[[1,0],[0,1]],[[1,0],[0,-1]],[[-1,0],[0,1]],[[-1,0],[0,-1]]],
[[[1,0],[-1,0],[0,1]],[[1,0],[-1,0],[0,-1]],[[1,0],[0,1],[0,-1]],[[-1,0],[0,1],[0,-1]]],
[[[1,0],[-1,0],[0,1],[0,-1]]]]



def recu(new_matrix,new_cctv_list):
	global min_zero

	if new_cctv_list == []:
		now_zero_cnt = 0

		for get_new_matrix in new_matrix:
			now_zero_cnt = now_zero_cnt + get_new_matrix.count(0)

		if now_zero_cnt < min_zero:
			min_zero = now_zero_cnt
			
		return

	pop_cctv = new_cctv_list.pop()

	ind_y = pop_cctv[0]
	ind_x = pop_cctv[1]
	cctv_pos = matrix[ind_y][ind_x]
	now_cctv_matix = cctv_matrix[cctv_pos-1]

	
	for get_cctv in now_cctv_matix:
		cp_matrix = [[] for col in range(N)]
		for idy, get_new_matrix in enumerate(new_matrix):
			cp_matrix[idy] = get_new_matrix[:]

		for cctv_dir in get_cctv:
			#print("cctv_dir",cctv_dir)
			

			tmp_ind_y = ind_y
			tmp_ind_x = ind_x
			while 1:
				new_y = tmp_ind_y + cctv_dir[0]
				new_x = tmp_ind_x + cctv_dir[1]

				if new_y < 0 or new_x <0 or new_x >= M or new_y >=N or cp_matrix[new_y][new_x]==6:
					break
				cp_matrix[new_y][new_x] = 9
				tmp_ind_y = new_y
				tmp_ind_x = new_x

		recu(cp_matrix,new_cctv_list[:])
	return 


N, M = map(int, sys.stdin.readline().split())
min_zero = 0
matrix = []
block_list = []
cctv_list = []

for idy in range(N):
	tmp_list = list(map(int, sys.stdin.readline().split()))
	matrix.append(tmp_list)
	for idx, get_list in enumerate(tmp_list):
		if get_list == 6:
			block_list.append([idy, idx])
		elif get_list == 0:
			min_zero = min_zero + 1
		else :
			cctv_list.append([idy, idx])

#print(cctv_list)
recu(matrix,cctv_list[:])
print(min_zero)