
N,L = map(int, input().split())
D = [[*map(int, input().split())] for _ in range(N)]


#(0,x) (x,0)
#(0~N-1,x) (x,0~N-1)  
cnt = 0
for y in range(N):
	right_flag=1
	right_visit = {}

	for x in range(N-1):
		#print("right",(y,x))
		right_idx = (y,x)
		if D[right_idx[0]][right_idx[1]] == D[right_idx[0]][right_idx[1]+1] :
			continue
		elif abs(D[right_idx[0]][right_idx[1]] - D[right_idx[0]][right_idx[1]+1]) == 1:
			right_ind_tmp = list(right_idx)

			if D[right_idx[0]][right_idx[1]] > D[right_idx[0]][right_idx[1]+1] :
				right_ind_tmp[1] = right_ind_tmp[1] + 1
				fix_val = D[right_ind_tmp[0]][right_ind_tmp[1]]
				#visit[tuple(right_ind_tmp)] = True

				if right_ind_tmp[1]+L > N :
					right_flag = 0
					break
				for _ in range(L):
					if fix_val != D[right_ind_tmp[0]][right_ind_tmp[1]] or tuple(right_ind_tmp) in right_visit:
						#print("fix",fix_val, right_ind_tmp, D[right_ind_tmp[0]][right_ind_tmp[1]])
						right_flag = 0
						break
					right_visit[tuple(right_ind_tmp)] = True
					right_ind_tmp[1] = right_ind_tmp[1] + 1



			elif D[right_idx[0]][right_idx[1]] < D[right_idx[0]][right_idx[1]+1]:
				fix_val = D[right_ind_tmp[0]][right_ind_tmp[1]]
				#visit[tuple(right_ind_tmp)] = True
				if right_ind_tmp[1]-L + 1 < 0 :
					right_flag = 0
					break
				for _ in range(L):
					if fix_val != D[right_ind_tmp[0]][right_ind_tmp[1]] or tuple(right_ind_tmp) in right_visit:
						right_flag = 0
						break
					right_visit[tuple(right_ind_tmp)] = True
					right_ind_tmp[1] = right_ind_tmp[1] - 1
		else :
			right_flag = 0
	if right_flag == 1:
		#print("right_flag",(y,x))
		cnt = cnt + 1 

	bottom_flag = 1
	bottom_visit = {}

	for x in range(N-1):
		right_idx = (x,y)
		if D[right_idx[0]][right_idx[1]] == D[right_idx[0]+1][right_idx[1]] :
			continue
		elif abs(D[right_idx[0]][right_idx[1]] - D[right_idx[0]+1][right_idx[1]]) == 1:
			right_ind_tmp = list(right_idx)

			if D[right_idx[0]][right_idx[1]] > D[right_idx[0]+1][right_idx[1]] :
				right_ind_tmp[0] = right_ind_tmp[0] + 1
				fix_val = D[right_ind_tmp[0]][right_ind_tmp[1]]
				#visit[tuple(right_ind_tmp)] = True
				if right_ind_tmp[0]+L > N :
					bottom_flag = 0
					break
				#print(right_ind_tmp)
				for _ in range(L):
					if fix_val != D[right_ind_tmp[0]][right_ind_tmp[1]] or tuple(right_ind_tmp) in bottom_visit:
						bottom_flag = 0
						break
					bottom_visit[tuple(right_ind_tmp)] = True
					right_ind_tmp[0] = right_ind_tmp[0] + 1

			
			elif D[right_idx[0]][right_idx[1]] < D[right_idx[0]+1][right_idx[1]]:
				fix_val = D[right_ind_tmp[0]][right_ind_tmp[1]]
				#visit[tuple(right_ind_tmp)] = True
				if right_ind_tmp[0]-L + 1 < 0 :
					bottom_flag = 0
					break
				for _ in range(L):
					if fix_val != D[right_ind_tmp[0]][right_ind_tmp[1]] or tuple(right_ind_tmp) in bottom_visit:
						bottom_flag = 0
						break
					bottom_visit[tuple(right_ind_tmp)] = True
					right_ind_tmp[0] = right_ind_tmp[0] - 1

		else :
			bottom_flag = 0
	if bottom_flag == 1:
		#print("bottom_flag",(x,y))

		cnt = cnt + 1 


		#bottom_idx = (x,y)

print(cnt)
	