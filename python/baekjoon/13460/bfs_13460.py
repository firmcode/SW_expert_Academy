from queue import Queue
import copy

min_cnt = 11
def bfs(D_val,r_val,b_val):
	dxy = [(0,1),(1,0),(-1,0),(0,-1)]
	visit = {}
	global min_cnt
	q = Queue()
	q.put((r_val[:],b_val[:]))
	visit[tuple(r_val),tuple(b_val)] = 0

	#print(visit[tuple(r_val),tuple(b_val)])

	while q.qsize() > 0:
		#print(q.get())
		cur_r, cur_b = q.get()

		for ixy in dxy :
			next_r = cur_r[:]
			next_b = cur_b[:]
			cur_r_cnt = cur_b_cnt = 0
			#print(next_r,next_b)
			while D_val[next_r[0]][next_r[1]] == '.': 
				next_r[0] = next_r[0] + ixy[0]
				next_r[1] = next_r[1] + ixy[1]
				cur_r_cnt = cur_r_cnt + 1

			while D_val[next_b[0]][next_b[1]] == '.':
				next_b[0] = next_b[0] + ixy[0]
				next_b[1] = next_b[1] + ixy[1]
				cur_b_cnt = cur_b_cnt + 1

			#print(next_r,next_b, ixy)

			if (D_val[next_b[0]][next_b[1]] == 'O'):
				continue

			if D_val[next_r[0]][next_r[1]] == 'O':
				if min_cnt > visit[tuple(cur_r),tuple(cur_b)] + 1:
					min_cnt = visit[tuple(cur_r),tuple(cur_b)] + 1
					return min_cnt

			next_r[0] = next_r[0] - ixy[0]
			next_r[1] = next_r[1] - ixy[1]
			next_b[0] = next_b[0] - ixy[0]
			next_b[1] = next_b[1] - ixy[1]

			if next_r == next_b:
				if cur_r_cnt > cur_b_cnt:
					next_r[0] = next_r[0] - ixy[0]
					next_r[1] = next_r[1] - ixy[1]
				else:
					next_b[0] = next_b[0] - ixy[0]
					next_b[1] = next_b[1] - ixy[1]

			if ((tuple(next_r),tuple(next_b)) in visit) :
				continue
			#print("put",tuple(next_r),tuple(next_b),visit[tuple(cur_r),tuple(cur_b)])
			visit[tuple(next_r),tuple(next_b)] = visit[tuple(cur_r),tuple(cur_b)] + 1
			if visit[tuple(next_r),tuple(next_b)] > 10:
				min_cnt = -1 
				return 
			q.put((next_r[:],next_b[:]))


n,m = map(int, input().split())
D = [[*map(str, list(input()))] for _ in range(n)]

for ix in range(n):
	for iy in range(m):
		if D[ix][iy] == 'R':
			D[ix][iy] = '.'
			r = [ix,iy]
		if D[ix][iy] == 'B':
			D[ix][iy] = '.'
			b = [ix,iy]


bfs(D,r,b)

if min_cnt == 11:
	print("-1")
else:
	print(min_cnt)