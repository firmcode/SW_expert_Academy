import sys
from itertools import combinations

dydx = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(pick_list):
	cp_matrix = [[0 for col in range(N)]for row in range(N)]
	visit = [[0 for col in range(N)]for row in range(N)]
	for idy, get_mat in enumerate(matrix):
		cp_matrix[idy] = get_mat[:]


	max_visit = 0
	enq_cnt = 0
	q=[]
	for get_pick in pick_list:
		q_y, q_x = get_pick[0],get_pick[1]
		q.append([q_y,q_x])
		visit[q_y][q_x] = 1

	while q!= []:
		
		pop_q = q.pop(0)
		now_y ,now_x = pop_q[0],pop_q[1]
		now_vist_val = visit[now_y][now_x]

		for get_dydx in dydx:
			new_y, new_x = now_y + get_dydx[0], now_x + get_dydx[1]

			if new_x <0 or new_y<0 or new_x >=N or new_y >= N:
				continue
			if cp_matrix[new_y][new_x] == 0 and visit[new_y][new_x] == 0:
				q.append([new_y,new_x])
				visit[new_y][new_x] = now_vist_val + 1
				cp_matrix[new_y][new_x] = 1
				enq_cnt = enq_cnt +1

				if max_visit < now_vist_val + 1:
					max_visit = now_vist_val + 1

				if zero_cnt - enq_cnt == 0:
					return max_visit -1

			elif cp_matrix[new_y][new_x] == 2 and visit[new_y][new_x] == 0:
				q.append([new_y,new_x])
				visit[new_y][new_x] = now_vist_val + 1
				cp_matrix[new_y][new_x] = 1

	return 50*50*2

def recur(now_cnt, pick_list, nonpick_list):
	global g_min_time, M

	cp_list = nonpick_list[:]
	combi_list=list(combinations(nonpick_list,M))
	
	for pick_list in combi_list:
		now_time = bfs(pick_list)
		if now_time < g_min_time:
			g_min_time = now_time



N ,M = map(int, sys.stdin.readline().split())

matrix = []
vir_list = []
vir_cnt = 0
zero_cnt = 0

g_min_time = 50*50*2

for idy in range(N):
	tmp = list(map(int, sys.stdin.readline().split()))
	matrix.append(tmp)

	for idx, get_val in enumerate(tmp):
		if get_val == 2:
			vir_list.append([idy,idx])
			vir_cnt = vir_cnt + 1
		elif get_val == 0:
			zero_cnt = zero_cnt + 1

if zero_cnt != 0:
	recur(0,[],vir_list[:])
else:
	g_min_time = 0 

if g_min_time == 5000:
	print(-1)
else:
	print(g_min_time)
