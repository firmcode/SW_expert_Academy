import sys
dydx = [[-1,0],[0,-1],[0,1],[1,0]]
def bfs():
	global fish_cnt
	global postion
	global g_cnt_time, fish_size,fish_eat,matrix

	vist = [[0 for col in range(N)]for row in range(N)]
	eatable = [[0 for col in range(N)]for row in range(N)]

	q = []
	new_q= []
	new_q.append(postion)
	vist[postion[0]][postion[1]] = 1

	find_check = 0
	
	while find_check==0:
		#print("new_q",new_q)

		if new_q == []:
			break
		q = new_q[:]
		new_q = []
		#g_cnt_time = g_cnt_time +1
		while q != []:

			pop_q = q.pop(0)

			now_y,now_x = pop_q[0],pop_q[1]
			now_vist_val = vist[now_y][now_x]
			for get_dydx in dydx:
				new_y, new_x = now_y+ get_dydx[0], now_x + get_dydx[1]

				if new_y <0 or new_x <0 or new_x >=N or new_y>=N:
					continue
				new_val = matrix[new_y][new_x]
				#print("new_val:", new_val ,[new_y,new_x])
				if new_val !=0 and new_val !=9 and new_val < fish_size:
					#print("find!!")
					find_check = 1
					eatable[new_y][new_x] = 1
					vist[new_y][new_x] = now_vist_val
				elif new_val <= fish_size and vist[new_y][new_x]==0:
					new_q.append([new_y,new_x])
					vist[new_y][new_x] = now_vist_val + 1

	#print("eatable",eatable)


	for idy in range(N):
		for idx in range(N):
			if eatable[idy][idx] ==1:
				fish_cnt = fish_cnt - 1
				fish_eat = fish_eat + 1
				if fish_size == fish_eat:
					fish_size = fish_size + 1
					fish_eat = 0
				matrix[idy][idx] = 9
				matrix[postion[0]][postion[1]] = 0

				g_cnt_time = g_cnt_time + vist[idy][idx]
				postion = [idy,idx]

				return 1

	return 0




N =  int(sys.stdin.readline())

matrix = []
postion = []
fish_list = []
fish_cnt = 0
g_cnt_time = 0
fish_size =2
fish_eat = 0

for idy in range(N):
	tmp =list(map(int, sys.stdin.readline().split()))
	matrix.append(tmp)
	for idx, val in enumerate(tmp):
		if val == 9:
			postion = [idy,idx]
		elif val != 0:
			fish_list.append([idy,idx,val])
			fish_cnt = fish_cnt +1

while 1 :
	if bfs() == 0:
		break

print(g_cnt_time)

