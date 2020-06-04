import sys 
dydx = [[],[-1,0],[1,0],[0,1],[0,-1]]
def sim():
	#sorted(shark_dic,reverse=False)
	new_shark_dic = {}
	new_matrix = [[0 for cols in range(C)] for row in range(R)]

	for z, get_shark in shark_dic.items():
		r, c, s, d = get_shark[0],get_shark[1],get_shark[2],get_shark[3]
		matrix[r][c] = 0

		new_r, new_c = r, c
		if d == 1 or d==2 :
			s = s % ((R-1)*2)
		else:
			s = s % ((C-1)*2)

		for get_s in range(s):

			new_r = new_r + dydx[d][0]
			new_c = new_c + dydx[d][1]

			if new_r < 0:
				new_r = 1
				d = 2
			elif new_c < 0:
				new_c = 1
				d = 3
			elif new_r >=R:
				new_r = R - 2
				d = 1
			elif new_c >=C:
				d = 4
				new_c = C - 2
		
		if new_matrix[new_r][new_c] == 0:
			new_matrix[new_r][new_c] = z
			new_shark_dic[z] = [new_r, new_c, s, d]


	'''
	new_shark_dic = {}
	for z, get_shark in shark_dic.items():
		r, c, s, d = get_shark[0],get_shark[1],get_shark[2],get_shark[3]
		if matrix[r][c] == 0:
			matrix[r][c] = z
			new_shark_dic[z] = [r, c, s, d]
		else:
			get_z = matrix[r][c]
			if get_z < z:
				del(new_shark_dic[get_z])
				matrix[r][c] = z
				new_shark_dic[z] = [r, c, s, d]
	'''
	return new_matrix,new_shark_dic


R,C,M = map(int, sys.stdin.readline().split())

matrix = [[0 for cols in range(C)] for row in range(R)]

shark_dic = {}
for idx in range(M):
	r, c, s, d, z = map(int, sys.stdin.readline().split())
	shark_dic[z]=[r-1, c-1, s, d]
	matrix[r-1][c-1] = z

sorted_list=sorted(shark_dic.items(),reverse=True)
new_shark_dic = {}
for key, val in sorted_list:
	new_shark_dic[key] = val
shark_dic = new_shark_dic

catch = 0
for now_x in range(C):
	'''
	print(now_x)
	for get_mat in matrix:
		print(get_mat)
	print(shark_dic)
	'''
	for get_r in range(R):
		if matrix[get_r][now_x]!=0:
			get_z = matrix[get_r][now_x]
			del(shark_dic[get_z])
			catch = catch + get_z
			matrix[get_r][now_x] = 0
			break
	matrix, shark_dic=sim()

print(catch)

