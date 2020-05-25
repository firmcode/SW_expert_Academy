import sys

N, M = map(int, sys.stdin.readline().split())

matrix = []

fig1 = [[[0,0],[1,0],[2,0],[3,0]],
		[[0,0],[0,1],[0,2],[0,3]]]
fig2 = [[[0,0],[0,1],[1,1],[1,0]]] 
fig3 = [[[0,0],[1,0],[2,0],[0,1]],
		[[0,0],[1,0],[2,0],[1,1]],
		[[0,0],[1,0],[2,0],[2,1]],
		[[0,1],[1,1],[2,1],[0,0]],
		[[0,1],[1,1],[2,1],[1,0]],
		[[0,1],[1,1],[2,1],[2,0]],
		[[1,0],[2,0],[0,1],[1,1]],
		[[0,0],[1,0],[1,1],[2,1]]]
fig4 = [[[1,0],[1,1],[1,2],[0,0]],
		[[1,0],[1,1],[1,2],[0,1]],
		[[1,0],[1,1],[1,2],[0,2]],
		[[0,0],[0,1],[0,2],[1,0]],
		[[0,0],[0,1],[0,2],[1,1]],
		[[0,0],[0,1],[0,2],[1,2]],
		[[0,0],[0,1],[1,1],[1,2]],
		[[1,0],[0,1],[1,1],[0,2]]]

for idx in range(N):
	matrix.append(list(map(int, sys.stdin.readline().split())))

max_val = 0
#fig1_0
if M >= 4:
	for get_x in range(M-4+1):
		for get_y in range(N):
			sum_val = 0
			for idx in range(4):
				sum_val = sum_val + matrix[get_y + fig1[0][idx][1]][get_x + fig1[0][idx][0]]
			if sum_val > max_val:
				max_val = sum_val

#fig1_1
if N >= 4:
	for get_x in range(M):
		for get_y in range(N-4+1):
			sum_val = 0
			for idx in range(4):
				sum_val = sum_val + matrix[get_y + fig1[1][idx][1]][get_x + fig1[1][idx][0]]
			if sum_val > max_val:
				max_val = sum_val
#fig2
if M >= 2 and N>=2:
	for get_x in range(M-2+1):
		for get_y in range(N-2+1):
			sum_val = 0
			for idx in range(4):
				sum_val = sum_val + matrix[get_y + fig2[0][idx][1]][get_x + fig2[0][idx][0]]
			if sum_val > max_val:
				max_val = sum_val
#fig3
if N >= 2 and M>=3:
	for get_x in range(M-3+1):
		for get_y in range(N-2+1):
			
			for idx_shape in range(8):
				sum_val = 0
				for idx in range(4):
					#print("x,y",get_x,get_y)
					#print(idx_shape,idx)
					#print("new_xy",get_y + fig3[idx_shape][idx][1], get_x + fig3[idx_shape][idx][0])
					sum_val = sum_val + matrix[get_y + fig3[idx_shape][idx][1]][get_x + fig3[idx_shape][idx][0]]
				if sum_val > max_val:
					max_val = sum_val
#fig4
if N >= 3 and M>=2:
	for get_x in range(M-2+1):
		for get_y in range(N-3+1):
			
			for idx_shape in range(8):
				sum_val = 0
				for idx in range(4):
					sum_val = sum_val + matrix[get_y + fig4[idx_shape][idx][1]][get_x + fig4[idx_shape][idx][0]]
				if sum_val > max_val:
					max_val = sum_val


print(max_val)

