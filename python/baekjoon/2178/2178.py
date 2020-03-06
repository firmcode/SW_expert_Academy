from queue import Queue

def bfs(graph, start_node):
	dxy = [(0,1),(1,0),(-1,0),(0,-1)]

	visit = {}
	visit[(0,0)]=1

	q = Queue()
	q.put(start_node)

	while q.qsize() > 0:
		node = q.get()

		if((n-1,m-1) == node):
			return visit[(n-1,m-1)]
		x,y = node
		#print("x,y :",x,y)
		for i in dxy:
			dx,dy = i
			nextx = dx + x
			nexty = dy + y
			#print((nextx,nexty))

			if((nextx >= 0) and (nexty>=0) and (nextx<=n-1) and (nexty <=m-1) and (graph[nextx][nexty]==1) and (((nextx,nexty) not in visit) or (node == (0,0)))):
				q.put((nextx,nexty))
				visit[(nextx,nexty)]=visit[node]+1
				#print((nextx,nexty,"qsize:",q.qsize()))

	return 0


n,m = map(int, input().split())

D = [[*map(int, list(input()))] for _ in range(n)]


start=(0,0)

cnt=bfs(D,start)


print(cnt)

