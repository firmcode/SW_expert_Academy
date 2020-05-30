import sys 

dydx = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(now_matrix):
	g_ch_cnt=0
	
	visit_list = [[0 for row in range(N)] for col in range(N)]
	for idy in range(N):
		for idx in range(N):

			if visit_list[idy][idx] ==1:
				continue
			q = []
			q.append([idy,idx])
			#visit_list.append([idy,idx])
			visit_list[idy][idx] =1
			now_change = []
			
			sum_val = 0
			ch_cnt = 0
			now_que = 0
			while q != []:
				pop_q = q.pop()

				now_y  = pop_q[0]
				now_x  = pop_q[1]

				now_val = now_matrix[now_y][now_x]

				
				for get_dydx in dydx:
					new_y = now_y + get_dydx[0]
					new_x = now_x + get_dydx[1]

					if new_x < 0 or new_y < 0 or new_y>=N or new_x>=N:
						continue

					new_val = now_matrix[new_y][new_x]
					dif_val = abs(now_val - new_val)
					if (dif_val >=L and dif_val <= R) and (visit_list[new_y][new_x]==0):
						if now_que == 0:
							now_que = 1
							now_change.append([now_y,now_x])
							sum_val = sum_val + now_matrix[now_y][now_x]
							ch_cnt = ch_cnt + 1

						q.append([new_y,new_x])
						visit_list[new_y][new_x]=1
						now_change.append([new_y,new_x])
						sum_val = sum_val + now_matrix[new_y][new_x]
						ch_cnt = ch_cnt + 1

			if ch_cnt != 0:
				g_ch_cnt = g_ch_cnt + ch_cnt
				ch_val = int(sum_val/ch_cnt)

				for get_change in now_change:
					ch_y = get_change[0]
					ch_x = get_change[1]
					now_matrix[ch_y][ch_x] = ch_val

	return now_matrix,g_ch_cnt


N,L,R = map(int, sys.stdin.readline().split())

matrix = []

for idy in range(N):
	matrix.append(list(map(int, sys.stdin.readline().split())))

ch_cnt =1
out_cnt = -1
while ch_cnt !=0 :
	matrix,ch_cnt = bfs(matrix)
	out_cnt = out_cnt +1

print(out_cnt)
