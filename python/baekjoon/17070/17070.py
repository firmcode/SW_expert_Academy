global cnt_num


def dfs(x,y,pre_state):

	if (x==n-1) and (y==n-1): #end
		global cnt_num

		cnt_num=cnt_num+1
		return 0



	if pre_state ==0: #search
		if (y+1 < n) and (D[x][y+1] ==0):
			dfs(x,y+1,0)
		if (x+1 < n) and (y+1 < n) and (D[x][y+1] ==0) and (D[x+1][y] ==0) and (D[x+1][y+1] ==0) :
			dfs(x+1,y+1,2)
	elif pre_state ==1:
		if (x+1 < n) and (D[x+1][y] ==0) :
			dfs(x+1,y,1)
		if (x+1 < n) and (y+1 < n) and (D[x][y+1] ==0) and (D[x+1][y] ==0) and (D[x+1][y+1] ==0):
			dfs(x+1,y+1,2)
	elif pre_state==2:
		if (y+1 < n) and (D[x][y+1] ==0):
			dfs(x,y+1,0)
		if (x+1 < n) and (D[x+1][y] ==0) :
			dfs(x+1,y,1)
		if (x+1 < n) and (y+1 < n) and (D[x][y+1] ==0) and (D[x+1][y] ==0) and (D[x+1][y+1] ==0):
			dfs(x+1,y+1,2)

	return 0

n = int(input())
D = [[*map(int, input().split())] for _ in range(n)]
cnt_num = 0
dfs(0,1,0)

print(cnt_num)
#print(D[0][2])

