import sys

g_min_dist = 50*50*2
def recur(pick_list,limit_cnt,now_cnt,pre_list_idx):
	global g_min_dist

	for list_idx in range(shop_cnt):
		if list_idx <= pre_list_idx and pre_list_idx!=0:
			continue
		pick_list.append(shop_list[list_idx])
		now_cnt = now_cnt + 1

		if limit_cnt <= now_cnt:
			min_sum = 0
			#print("pick_list",pick_list)
			for get_home in home_list:
				home_y = get_home[0]
				home_x = get_home[1]
				min_dis = 101
				
				for get_pick in pick_list:
					shop_y = get_pick[0]
					shop_x = get_pick[1]
					now_dist = abs(home_y - shop_y) + abs(home_x - shop_x)
					if now_dist < min_dis:
						min_dis  = now_dist
				min_sum = min_sum + min_dis

			if g_min_dist > min_sum :
				g_min_dist = min_sum
		else:
			recur(pick_list[:],limit_cnt,now_cnt,list_idx)
		pick_list.remove(shop_list[list_idx])
		now_cnt = now_cnt - 1



N,M=map(int, sys.stdin.readline().split())

matrix = [[] for row in range(N)]

home_list = []
shop_list = []
shop_cnt = 0 

for idy in range(N):
	tmp_list = list(map(int, sys.stdin.readline().split()))
	matrix.append(tmp_list)
	for idx ,get_val in enumerate(tmp_list):
		if get_val == 1:
			home_list.append([idy,idx])
		elif get_val ==2:
			shop_list.append([idy,idx])
			shop_cnt = shop_cnt+1


recur([],M,0,0)
print(g_min_dist)
