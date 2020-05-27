import sys

dxdy = [[-1,0],[0,1],[1,0],[0,-1]]
g_cnt = 0
def bfs():
	global g_cnt
	visit = [[0 for col in range(C)] for row in range(R)]

	q = []

	q.append([bot_r, bot_c,bot_dir])
	visit[bot_r][bot_c] = 5
	matrix[bot_r][bot_c] = 5
	g_cnt = g_cnt + 1
	#print("g_cnt",g_cnt)

	while q !=[]:
		get_q = q.pop()

		now_y = get_q[0]
		now_x = get_q[1]
		now_dir = get_q[2]

		#for ind in range(R):
			#print(matrix[ind])


		check_append = 0
		for search_idx in range(4):

			new_dir = (now_dir - (search_idx+1))%4
			new_y = now_y + dxdy[new_dir][0]
			new_x = now_x + dxdy[new_dir][1]
			
			if visit[new_y][new_x] == 0 and matrix[new_y][new_x]==0:
				q.append([new_y, new_x,new_dir])
				visit[new_y][new_x] = 5
				matrix[new_y][new_x] = 5
				g_cnt = g_cnt + 1
				check_append = 1
				break

			if search_idx == 3 and check_append == 0:
				back_y = now_y - dxdy[new_dir][0]
				back_x = now_x - dxdy[new_dir][1]
				if matrix[back_y][back_x] == 1:
					return
				else :
					q.append([back_y, back_x,new_dir])

			if visit[new_y][new_x] != 0 or matrix[new_y][new_x]!=0:
				#q.append([now_y, now_x,new_dir])
				continue




R, C = map(int, sys.stdin.readline().split())

bot_r, bot_c, bot_dir = map(int, sys.stdin.readline().split())
matrix = []
for idx in range(R):
	matrix.append(list(map(int, sys.stdin.readline().split())))

bfs()
print(g_cnt)

