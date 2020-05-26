'''
   0
 0 0 0
   0
   0

   0
 0 0 0
   3
   0

   0
 0 5 0
   3
   0

   7
 0 5 0
   3
   0

   7
 0 5 8
   3
   0

   7
 0 6 8
   3
   0

   7
 4 6 8
   3
   0

   7
 4 6 8
   3
   2
'''
import sys
dice_top = 0
dice_front = 0
dice_bot = 0
dice_behind = 0
dice_left = 0
dice_right = 0

new_top = 0
new_front = 0
new_bot = 0
new_behind = 0
new_left = 0
new_right = 0

dxdy = [[0,1],[0,-1],[-1,0],[1,0]]
def swap():
	global dice_top,dice_front,dice_bot,dice_behind,dice_left,dice_right
	global new_top,new_front,new_bot,new_behind,new_left,new_right
	dice_top = new_top
	dice_front = new_front
	dice_bot = new_bot
	dice_behind = new_behind
	dice_left = new_left
	dice_right = new_right

def rot1():
	global dice_top,dice_front,dice_bot,dice_behind,dice_left,dice_right
	global new_top,new_front,new_bot,new_behind,new_left,new_right
	new_top = dice_left
	new_front = dice_front
	new_bot = dice_right
	new_behind = dice_behind
	new_left = dice_bot
	new_right = dice_top
	swap()

def rot2():
	global dice_top,dice_front,dice_bot,dice_behind,dice_left,dice_right
	global new_top,new_front,new_bot,new_behind,new_left,new_right
	new_top = dice_right
	new_front = dice_front
	new_bot = dice_left
	new_behind = dice_behind
	new_left = dice_top
	new_right = dice_bot
	swap()

def rot3():
	global dice_top,dice_front,dice_bot,dice_behind,dice_left,dice_right
	global new_top,new_front,new_bot,new_behind,new_left,new_right
	new_top = dice_front
	new_front = dice_bot
	new_bot = dice_behind
	new_behind = dice_top
	new_left = dice_left
	new_right = dice_right
	swap()

def rot4():
	global dice_top,dice_front,dice_bot,dice_behind,dice_left,dice_right
	global new_top,new_front,new_bot,new_behind,new_left,new_right
	new_top = dice_behind
	new_front = dice_top
	new_bot = dice_front
	new_behind = dice_bot
	new_left = dice_left
	new_right = dice_right
	swap()

N,M, y,x, k = map(int, sys.stdin.readline().split())

matrix = [[] for row in range(N)]

for idy in range(N):
	matrix[idy] = list(map(int, sys.stdin.readline().split()))

command = list(map(int, sys.stdin.readline().split()))

if matrix[y][x] == 0 :
	matrix[y][x] = dice_bot
else :
	dice_bot = matrix[y][x]
	matrix[y][x] = 0

for get_comm in command:
	x = x + dxdy[get_comm-1][1]
	y = y + dxdy[get_comm-1][0]
	#print("xy",x,y)
	if (x <0) or (y <0) or (x>=M) or (y>=N):
		x = x - dxdy[get_comm-1][1]
		y = y - dxdy[get_comm-1][0]
		continue
	if get_comm == 1:
		rot1()
		if matrix[y][x] == 0 :
			matrix[y][x] = dice_bot
		else :
			dice_bot = matrix[y][x]
			matrix[y][x] = 0
		print(dice_top)
	elif get_comm == 2:
		rot2()
		if matrix[y][x] == 0 :
			matrix[y][x] = dice_bot
		else :
			dice_bot = matrix[y][x]
			matrix[y][x] = 0
		print(dice_top)
	elif get_comm == 3:
		rot3()
		if matrix[y][x] == 0 :
			matrix[y][x] = dice_bot
		else :
			dice_bot = matrix[y][x]
			matrix[y][x] = 0
		print(dice_top)
	elif get_comm == 4:
		rot4()
		if matrix[y][x] == 0 :
			matrix[y][x] = dice_bot
		else :
			dice_bot = matrix[y][x]
			matrix[y][x] = 0
		print(dice_top)







