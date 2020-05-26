import sys
import queue
import copy

dxdy = [[0,1],[0,-1],[-1,0],[1,0]]

#min_cnt = 100000
def bfs(matrix):
	#global min_cnt
	tmp = copy.deepcopy(matrix)

	'''
	tmp = [[] for row in range(N)]
	for idx in range(N):
		tmp[idx] = matrix[idx][:]
	'''
	#q = queue.Queue()
	q = []
	#visit = []
	#visit = [[0 for col in range(M)] for row in range(N)]


	for get_poi_xy in poi_xy:
		#q.put(get_poi_xy)
		q.append(get_poi_xy)
		#visit.append(get_poi_xy)
		#y=get_poi_xy[0]
		#x=get_poi_xy[1]

		#visit[y][x] = 1

	cnt = 0

	#while q.empty() == False:
	while q !=[]:
		#poi_get = q.get()
		poi_get = q.pop()

		y=poi_get[0]
		x=poi_get[1]

		for get_dxdy in dxdy:
			next_y = y + get_dxdy[0]
			next_x = x + get_dxdy[1]
			if (next_y >= N) or (next_x >= M) or (next_x < 0) or (next_y < 0):
				continue

			#if matrix[next_y][next_x] == 0 and ([next_y,next_x] not in visit):
			if tmp[next_y][next_x] == 0:
			#if matrix[next_y][next_x] == 0 and (visit[next_y][next_x]==0):
				tmp[next_y][next_x]=2
				#q.put([next_y,next_x])
				q.append([next_y,next_x])
				#visit.append([next_y,next_x])
				cnt = cnt+1
				#if cnt > min_cnt:
				#	return 0

	#for idx in range(N):
	#	print(tmp[idx])
	#if min_cnt > cnt :
	#	min_cnt = cnt

	saf_cnt = N*M - cnt - poi_xy_len - block_cnt
	return saf_cnt

max_cnt = 0
def make_block(block_numb,new_matrix,y,x):
	global max_cnt
	zero_len=len(zero_list)
	for get_one in range(zero_len):
		idy1 = zero_list[get_one][0]
		idx1 = zero_list[get_one][1]
		new_matrix[idy1][idx1] = 1

		for get_two in range(get_one+1,zero_len):
			idy2 = zero_list[get_two][0]
			idx2 = zero_list[get_two][1]
			new_matrix[idy2][idx2] = 1
			for get_thr in range(get_two+1,zero_len):
				idy3 = zero_list[get_thr][0]
				idx3 = zero_list[get_thr][1]
				new_matrix[idy3][idx3] = 1

				now_saf_cnt = bfs(new_matrix) - 3
				#print(now_saf_cnt)
				if max_cnt < now_saf_cnt:
					max_cnt = now_saf_cnt

				new_matrix[idy3][idx3] = 0
			new_matrix[idy2][idx2] = 0
		new_matrix[idy1][idx1] = 0


N,M = map(int, sys.stdin.readline().split())

matrix = [[0 for col in range(M)] for row in range(N)]
poi_xy = []
block_cnt = 0
zero_list = []
for idy in range(N):
	tmp = list(map(int, sys.stdin.readline().split()))
	for idx in range(M):
		matrix[idy][idx] = tmp[idx]
		if tmp[idx] == 2:
			poi_xy.append([idy,idx])
		elif tmp[idx] == 1:
			block_cnt = block_cnt + 1
		else:
			zero_list.append([idy,idx])
poi_xy_len = len(poi_xy)


make_block(0,matrix,0,0)

print(max_cnt)

'''
tmp_matrix = [[2, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 2],
[1, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0]]

print(bfs(tmp_matrix))
'''