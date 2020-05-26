import sys


dxdy = [[0,1],[-1,0],[0,-1],[1,0]]
def sim():
	now_dir = 0
	q = []
	q.append([0,0])
	sim_matrix[0][0] = 1
	total_sec = 0

	pre_sec = 0

	dir_list_ind = 0
	get_dir = dir_list[dir_list_ind]
	sec = get_dir[0]
	dir_str = get_dir[1]

	for idx in range(10000):
		total_sec = total_sec + 1
		
		get_front = q[-1]
		now_y = get_front[0]
		now_x = get_front[1]
		next_y = now_y + dxdy[now_dir][0]
		next_x = now_x + dxdy[now_dir][1]

		if (next_y >= N) or (next_x >= N) or (next_y <= -1) or (next_x <= -1):
			#print("return1")
			return total_sec
		if sim_matrix[next_y][next_x] == 5:
			q.append([next_y,next_x])
			sim_matrix[next_y][next_x] = 1
		elif sim_matrix[next_y][next_x] == 1:
			#print("return2")
			return total_sec
		else :
			q.append([next_y,next_x])
			sim_matrix[next_y][next_x] = 1

			get_tail = q[0]
			tail_y = get_tail[0]
			tail_x = get_tail[1]
			q.remove([tail_y, tail_x])
			sim_matrix[tail_y][tail_x] = 0

		#print(total_sec)
		#for get_ma in sim_matrix:
		#	print(get_ma)

		if sec == total_sec : 
			if dir_str == 'L':
				now_dir = (now_dir + 1)%4
			else:
				now_dir = (now_dir - 1)%4

			if dir_list_ind < dir_cnt-1:
				dir_list_ind = dir_list_ind + 1
				get_dir = dir_list[dir_list_ind]
				sec = get_dir[0]
				dir_str = get_dir[1]


	return total_sec



N = int(sys.stdin.readline())

sim_matrix = [[0 for col in range(N)]for row in range(N)]

apple_cnt = int(sys.stdin.readline())

apple_list = []
for idx in range(apple_cnt):
	y,x = map(int, sys.stdin.readline().split())
	sim_matrix[y-1][x-1] = 5


dir_cnt = int(sys.stdin.readline())
dir_list = []
for idx in range(dir_cnt):
	sec, dir_str = map(str, sys.stdin.readline().split())
	dir_list.append([int(sec),dir_str])

print(sim())
