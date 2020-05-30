import sys

dydx = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
N,M,K = map(int, sys.stdin.readline().split())

matrix = [[5 for col in range(N)]for row in range(N)]
cp_matrix = []
output_sum = 0 

for row in range(N):
	tmp = list(map(int, sys.stdin.readline().split()))
	cp_matrix.append(tmp)

tree_list = [[[] for row in range(N)] for row in range(N)]
for get_m in range(M):
	idy, idx, age = list(map(int, sys.stdin.readline().split()))
	output_sum = output_sum + 1
	if tree_list[idy-1][idx-1] == []:
		tree_list[idy-1][idx-1].append(age)
	else: 
		enqu = 0
		for ind, get_val in enumerate(tree_list[idy-1][idx-1]):
			if age <= get_val:
				tree_list[idy-1][idx-1].insert(ind+1,age)
				enqu =1
				break
		if enqu == 0:
			tree_list[idy-1][idx-1].insert(0,age)


#print("first tree_list",tree_list)
for get_k in range(K):
	#atum
	dead_tree = []
	for tree_y in range(N):
		for tree_x in range(N):
			if tree_list[tree_y][tree_x] == [] :
				continue
			new_age = []
			while tree_list[tree_y][tree_x]!=[]:
				#min_age = min(tree_list[tree_y][tree_x])
				#tree_list[tree_y][tree_x].remove(min_age)
				min_age = tree_list[tree_y][tree_x].pop()
				#print("min_age",min_age)
				if matrix[tree_y][tree_x] >= min_age:
					matrix[tree_y][tree_x] = matrix[tree_y][tree_x] - min_age
					#new_age.insert(0,min_age+1)
					new_age.append(min_age+1)
					#new_age = [min_age+1] + new_age[:]
				else:
					output_sum = output_sum -1
					dead_tree.append([tree_y,tree_x,min_age])

			#new_age.sort()
			new_age.reverse()
			tree_list[tree_y][tree_x] = new_age
			#print("new_age",new_age)
	#print("dead_tree",dead_tree)
	for get_dead in dead_tree:
		dead_y,dead_x,dead_age = get_dead[0],get_dead[1],get_dead[2]
		matrix[dead_y][dead_x] = matrix[dead_y][dead_x] + int(dead_age/2)

	for tree_y in range(N):
		for tree_x in range(N):
			if tree_list[tree_y][tree_x] == []:
				continue
			for tree_age in tree_list[tree_y][tree_x]:
				if tree_age%5 == 0:
					for get_dydx in dydx:
						new_tree_y = tree_y + get_dydx[0]
						new_tree_x = tree_x + get_dydx[1]
						if new_tree_y < 0 or new_tree_x < 0 or new_tree_x >=N or new_tree_y >= N:
							continue
						output_sum = output_sum + 1
						tree_list[new_tree_y][new_tree_x].append(1)

	for tree_y in range(N):
		for tree_x in range(N): 
			matrix[tree_y][tree_x] = matrix[tree_y][tree_x] + cp_matrix[tree_y][tree_x]
	#print("tree_list",tree_list)

#print("tree_list",tree_list)


print(output_sum)
