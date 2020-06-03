import sys 
def f1(x):
	return x[1]

def R_comput(matrix):
	global now_r, now_c
	max_col = 0
	
	for idy in range(now_r):
		dic_cnt = dict()

		for idx in range(now_c):
			get_val = matrix[idy][idx]
			if get_val == 0 :
				continue
			if get_val in dic_cnt:
				dic_cnt[get_val] = dic_cnt[get_val] + 1
			else:
				dic_cnt[get_val] = 1

		new_list = []
		sort_dic = sorted(dic_cnt.items(), key = f1)
		tmp_list = []
		sort_dic_len = len(sort_dic)
		for idx in range(sort_dic_len):
			if idx == sort_dic_len-1:
				if sort_dic[idx][1] == sort_dic[idx-1][1]:
					tmp_list.append(sort_dic[idx][0])
				if tmp_list !=[]:
					tmp_list.sort()
					for get_val in tmp_list:
						new_list.append(get_val)
						new_list.append(sort_dic[idx][1])
				else :
					new_list.append(sort_dic[idx][0])
					new_list.append(sort_dic[idx][1])
			elif sort_dic[idx][1] == sort_dic[idx+1][1]:
				tmp_list.append(sort_dic[idx][0])
			elif tmp_list !=[]:
				tmp_list.append(sort_dic[idx][0])
				tmp_list.sort()
				for get_val in tmp_list:
					new_list.append(get_val)
					new_list.append(sort_dic[idx][1])
				tmp_list = []
			else :
				new_list.append(sort_dic[idx][0])
				new_list.append(sort_dic[idx][1])

		new_list_len = len(new_list)
		if new_list_len >= 100:
			new_list_len = 100
		for idx in range(new_list_len):
			matrix[idy][idx] = new_list[idx]

		if new_list_len < now_c:
			for zero_idx in range(new_list_len,now_c):
				matrix[idy][zero_idx] = 0

		if new_list_len > max_col :
			max_col = new_list_len

	now_c = max_col
	return matrix

def C_comput(matrix):
	global now_r, now_c
	max_row = 0
	
	for now_idx in range(now_c):
		dic_cnt = dict()

		for idy in range(now_r):
			get_val = matrix[idy][now_idx]
			if get_val == 0 :
				continue
			if get_val in dic_cnt:
				dic_cnt[get_val] = dic_cnt[get_val] + 1
			else:
				dic_cnt[get_val] = 1

		new_list = []
		sort_dic = sorted(dic_cnt.items(), key = f1)
		tmp_list = []

		sort_dic_len = len(sort_dic)
		for idx in range(sort_dic_len):
			if idx == sort_dic_len-1:
				if sort_dic[idx][1] == sort_dic[idx-1][1]:
					tmp_list.append(sort_dic[idx][0])
				if tmp_list !=[]:
					tmp_list.sort()
					for get_val in tmp_list:
						new_list.append(get_val)
						new_list.append(sort_dic[idx][1])
				else :
					new_list.append(sort_dic[idx][0])
					new_list.append(sort_dic[idx][1])
			elif sort_dic[idx][1] == sort_dic[idx+1][1]:
				tmp_list.append(sort_dic[idx][0])
			elif tmp_list !=[]:
				tmp_list.append(sort_dic[idx][0])
				tmp_list.sort()
				for get_val in tmp_list:
					new_list.append(get_val)
					new_list.append(sort_dic[idx][1])
				tmp_list = []
			else :
				new_list.append(sort_dic[idx][0])
				new_list.append(sort_dic[idx][1])

		new_list_len = len(new_list)
		if new_list_len >= 100:
			new_list_len = 100
		for idy in range(new_list_len):
			matrix[idy][now_idx] = new_list[idy]

		if new_list_len < now_r:
			for zero_idy in range(new_list_len,now_r):
				matrix[zero_idy][now_idx] = 0

		if new_list_len > max_row :
			max_row = new_list_len
	now_r = max_row
	return matrix




r,c,k = map(int, sys.stdin.readline().split())

matrix = [[0 for col in range(100)] for row in range(100)]

for idy in range(3):
	tmp = list(map(int, sys.stdin.readline().split()))
	for idx, get_tmp in enumerate(tmp):
		matrix[idy][idx] = get_tmp

now_r = 3
now_c = 3

now_time = 0

if matrix[r-1][c-1] == k:
	print(0)

else :
	while matrix[r-1][c-1]!= k:

		if now_r >= now_c:
			matrix = R_comput(matrix)
		elif now_r < now_c:
			matrix = C_comput(matrix)
		now_time = now_time +1
		if now_time >100:
			now_time = -1
			break
	print(now_time)

'''
matrix=R_comput(matrix)
for idy in range(now_r):
	print(matrix[idy][:now_c])
print("")

matrix=C_comput(matrix)
for idy in range(now_r):
	print(matrix[idy][:now_c])
print("")
matrix=R_comput(matrix)
for idy in range(now_r):
	print(matrix[idy][:now_c])
print("")
matrix=R_comput(matrix)
for idy in range(now_r):
	print(matrix[idy][:now_c])
'''