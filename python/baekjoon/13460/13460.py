from queue import Queue
import copy

min_cnt = 11
def dfs(D_val,b_val,r_val,cnt,current_dir):
	global min_cnt
	if cnt >= min_cnt:
		return 0;


	if b_val == [-1,-1]:
		return 0
	if r_val == [-1,-1]:

		if min_cnt > cnt:
			min_cnt = cnt
		return 0


	

	cnt = cnt + 1


	dxy = [(0,1),(1,0),(-1,0),(0,-1)]
	if current_dir != []:
		dxy.remove(current_dir)
		if current_dir == (0,1):
			dxy.remove((0,-1))
		elif current_dir == (0,-1):
			dxy.remove((0,1))
		elif current_dir == (1,0):
			dxy.remove((-1,0))
		elif current_dir == (-1,0):
			dxy.remove((1,0))


	#print(cnt, r_val, b_val, "dxy",dxy)


	#print("dxy",dxy)
	for ixy in dxy:
		#print(cnt, r_val, b_val, "dxy",dxy, "D_val : ",D_val[4][1],D_val[4][2], "ixy" , ixy)
		D = copy.deepcopy(D_val)
		b = b_val[:]
		r = r_val[:]
		if ixy == (0,1):
			if b[1] > r[1]:
				D[b[0]][b[1]] = '.'
				#while (D[b[0]][b[1]] == '.') and :
				while D[b[0]][b[1]] == '.':
					b[1] = b[1] + 1
					#print("b in while",b,r)

				if D[b[0]][b[1]] == 'O':
					b = [-1,-1]
				else:
					b[1] = b[1] -1
					D[b[0]][b[1]] = 'B'

				D[r[0]][r[1]] = '.'
				while D[r[0]][r[1]] == '.':
					r[1] = r[1] + 1
					#print("in while",b,r)
				if D[r[0]][r[1]] == 'O':
					r = [-1,-1]
				else:
					r[1] = r[1] - 1
					D[r[0]][r[1]] = 'R'

				#print(b,r)
				
			else:
				D[r[0]][r[1]] = '.'
				while D[r[0]][r[1]] == '.':
					r[1] = r[1] + 1
				if D[r[0]][r[1]] == 'O':
					r = [-1,-1]
				else:
					r[1] = r[1] - 1
					D[r[0]][r[1]] = 'R'

				D[b[0]][b[1]] = '.'
				while D[b[0]][b[1]] == '.':
					b[1] = b[1] + 1
				if D[b[0]][b[1]] == 'O':
					b = [-1,-1]
				else:
					b[1] = b[1] -1
					D[b[0]][b[1]] = 'B'
		elif ixy == (1,0):
			if b[0] > r[0]:
				D[b[0]][b[1]] = '.'
				while D[b[0]][b[1]] == '.':
					b[0] = b[0] + 1
				if D[b[0]][b[1]] == 'O':
					b = [-1,-1]
				else:
					b[0] = b[0] - 1
					D[b[0]][b[1]] = 'B'

				D[r[0]][r[1]] = '.'
				while D[r[0]][r[1]] == '.':
					r[0] = r[0] + 1
				if D[r[0]][r[1]] == 'O':
					r = [-1,-1]
				else:
					r[0] = r[0] -1 
					D[r[0]][r[1]] = 'R'
				
			else:
				D[r[0]][r[1]] = '.'
				while D[r[0]][r[1]] == '.':
					r[0] = r[0] + 1
				if D[r[0]][r[1]] == 'O':
					r = [-1,-1]
				else:
					r[0] = r[0] -1 
					D[r[0]][r[1]] = 'R'

				D[b[0]][b[1]] = '.'
				while D[b[0]][b[1]] == '.':
					b[0] = b[0] + 1
					#print("b in while", b)
				if D[b[0]][b[1]] == 'O':
					b = [-1,-1]
				else:
					b[0] = b[0] - 1
					D[b[0]][b[1]] = 'B'
		elif ixy == (0,-1):
			if b[1] < r[1]:
				D[b[0]][b[1]] = '.'
				while D[b[0]][b[1]] == '.':
					b[1] = b[1] - 1
				if D[b[0]][b[1]] == 'O':
					b = [-1,-1]
				else:
					b[1] = b[1] + 1
					D[b[0]][b[1]] = 'B'

				D[r[0]][r[1]] = '.'
				while D[r[0]][r[1]] == '.':
					r[1] = r[1] - 1
				if D[r[0]][r[1]] == 'O':
					r = [-1,-1]
				else:
					r[1] = r[1] + 1
					D[r[0]][r[1]] = 'R'
			else:
				D[r[0]][r[1]] = '.'
				while D[r[0]][r[1]] == '.':
					r[1] = r[1] - 1
				if D[r[0]][r[1]] == 'O':
					r = [-1,-1]
				else:
					r[1] = r[1] + 1
					D[r[0]][r[1]] = 'R'
				
				D[b[0]][b[1]] = '.'
				while D[b[0]][b[1]] == '.':
					b[1] = b[1] - 1
				if D[b[0]][b[1]] == 'O':
					b = [-1,-1]
				else:
					b[1] = b[1] + 1
					D[b[0]][b[1]] = 'B'	
		elif ixy == (-1,0):
			if b[0] < r[0]:
				D[b[0]][b[1]] = '.'
				while D[b[0]][b[1]] == '.':
					b[0] = b[0] - 1
				if D[b[0]][b[1]] == 'O':
					b = [-1,-1]
				else:
					b[0] = b[0] + 1
					D[b[0]][b[1]] = 'B'

				D[r[0]][r[1]] = '.'
				while D[r[0]][r[1]] == '.':
					r[0] = r[0] - 1
				if D[r[0]][r[1]] == 'O':
					r = [-1,-1]
				else:
					r[0] = r[0] + 1
					D[r[0]][r[1]] = 'R'
				
			else:
				D[r[0]][r[1]] = '.'
				while D[r[0]][r[1]] == '.':
					r[0] = r[0] - 1
				if D[r[0]][r[1]] == 'O':
					r = [-1,-1]
				else:
					r[0] = r[0] + 1
					D[r[0]][r[1]] = 'R'

				D[b[0]][b[1]] = '.'
				while D[b[0]][b[1]] == '.':
					b[0] = b[0] - 1
				if D[b[0]][b[1]] == 'O':
					b = [-1,-1]
				else:
					b[0] = b[0] + 1
					D[b[0]][b[1]] = 'B'

		if (b != b_val) or (r != r_val):
			dfs(D[:],b,r,cnt,ixy[:])		

n,m = map(int, input().split())
D = [[*map(str, list(input()))] for _ in range(n)]

for ix in range(n):
	for iy in range(m):
		if D[ix][iy] == 'R':
			r = [ix,iy]
		if D[ix][iy] == 'B':
			b = [ix,iy]
		if D[ix][iy] == 'O':
			escape_ind = (ix,iy)


dfs(D,b,r,0,[])
if min_cnt == 11:
	print("-1")
else:
	print(min_cnt)