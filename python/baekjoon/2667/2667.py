from queue import Queue

def bfs(D, start_node):
	q = Queue()
	q.put(start_node)
	x,y = start_node
	D[x][y] = 0
	apart_cnt = 1

	while q.qsize() > 0:
		dxy = [(1,0),(0,1),(-1,0),(0,-1)]
		current_node = q.get()
		current_x, current_y = current_node

		for i in dxy:
			dx, dy = i
			next_x = current_x + dx
			next_y = current_y + dy
			if(next_x >= 0) and (next_y >= 0) and (next_x < n) and (next_y < n) and (D[next_x][next_y]==1):
				q.put((next_x,next_y))
				D[next_x][next_y] = 0
				apart_cnt = apart_cnt +1
	return apart_cnt

n = int(input())
D = [[*map(int, list(input()))] for _ in range(n)]

cnt = 0
cnt_apart = []

for x in range(n):
	for y in range(n):
		if(D[x][y] == 1):
			cnt_apart.append(bfs(D, (x,y)))
			cnt = cnt + 1

#print(n)

cnt_apart.sort()
print(cnt)
for i in cnt_apart:
	print(i)

