from queue import Queue
import copy

def propagation(D_val):
	dxy = [(1,0),(0,1),(-1,0),(0,-1)]
	new_D = [[0 for col in range(C)] for _ in range(R)]

	for in_x in range(R):
		for in_y in range(C):

			if D_val[in_x][in_y] > 0:
				move_cnt = 0 
				move_dust = int(D_val[in_x][in_y]/5)
				for idx in dxy:
					next_x = in_x + idx[0]
					next_y = in_y + idx[1]
					if next_x >= 0 and next_x < R and next_y >= 0 and next_y < C and D_val[next_x][next_y] != -1 :
						#print("move", next_x, next_y, move_dust,idx)
						new_D[next_x][next_y] = new_D[next_x][next_y] + move_dust
						move_cnt = move_cnt + 1
				new_D[in_x][in_y] = new_D[in_x][in_y] + (D_val[in_x][in_y] - move_dust * move_cnt)

	return new_D

def clean(pro_D, clean_ind1,clean_ind2):
	ind_x = clean_ind1[0] 
	ind_y = clean_ind1[1] 

	pro_D[ind_x][ind_y] = -1
	while 1:
		ind_x = ind_x - 1
		if(ind_x <=0):
			break
		pro_D[ind_x][ind_y] = pro_D[ind_x-1][ind_y]
		#print(ind_x,ind_y)

	while 1:
		if(ind_y >= C - 1):
			break
		pro_D[ind_x][ind_y] = pro_D[ind_x][ind_y+1]
		ind_y = ind_y + 1

		#print(ind_x,ind_y)


	while 1:
		if(ind_x >= clean_ind1[0]):
			break
		pro_D[ind_x][ind_y] = pro_D[ind_x+1][ind_y]
		ind_x = ind_x + 1
		#print(ind_x,ind_y)


	while 1:
		if(ind_y <= 1):
			break
		pro_D[ind_x][ind_y] = pro_D[ind_x][ind_y-1]
		ind_y = ind_y - 1 
		#print(ind_x,ind_y)
	pro_D[ind_x][ind_y] = 0

	ind_x = clean_ind2[0] 
	ind_y = clean_ind2[1] 

	pro_D[ind_x][ind_y] = -1

	while 1:
		if(ind_x >= R - 1):
			break
		pro_D[ind_x][ind_y] = pro_D[ind_x+1][ind_y]
		ind_x = ind_x + 1
		#print(ind_x,ind_y)

	while 1:
		if(ind_y >= C - 1):
			break
		pro_D[ind_x][ind_y] = pro_D[ind_x][ind_y+1]
		ind_y = ind_y + 1

		#print(ind_x,ind_y)

	while 1:
		if(ind_x <= clean_ind2[0]):
			break
		pro_D[ind_x][ind_y] = pro_D[ind_x-1][ind_y]
		ind_x = ind_x - 1

		#print(ind_x,ind_y)

	while 1:
		if(ind_y <= 1):
			break
		pro_D[ind_x][ind_y] = pro_D[ind_x][ind_y-1]
		ind_y = ind_y - 1
		#print(ind_x,ind_y)
	pro_D[ind_x][ind_y] = 0
	pro_D[clean_ind2[0]][clean_ind2[1]] = -1


	return pro_D


R,C, T = map(int, input().split())
D = [[*map(int, input().split())] for _ in range(R)]


clean_ind2=clean_ind1=[]
for in_x in range(R):
	for in_y in range(C):
		if D[in_x][in_y] == -1:
			clean_ind1 = [in_x,in_y]
			clean_ind2 = [in_x + 1,in_y]
			break
	if clean_ind1 != []:
		break

for i in range(T):
	pro_D = propagation(D)
	clean_D = clean(pro_D,clean_ind1,clean_ind2)
	D = clean_D
'''
for in_x in pro_D:
	print(in_x)
'''
dust_cnt = 0
for in_x in range(R):
	for in_y in range(C):
		if clean_D[in_x][in_y] > 0 :
			dust_cnt = dust_cnt + clean_D[in_x][in_y]

print(dust_cnt)
