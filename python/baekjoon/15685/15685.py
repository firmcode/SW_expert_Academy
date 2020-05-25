import sys

dic_matrix = {}
new_dic_matrix = {}

def cnt_squ():
	cnt = 0
	for get_dic in new_dic_matrix:

		x,y = get_dic[0],get_dic[1]
		#print(x,y)
		if ((x+1,y) in new_dic_matrix) and ((x+1,y-1) in new_dic_matrix) and ((x,y-1) in new_dic_matrix):
			cnt = cnt + 1
	print(cnt)
	#print(cnt_squ)


dydy=[[1,0],[0,-1],[-1,0],[0,1]]

def plot_cur(dra_cur):
	for get_cur in dra_cur:
		x = get_cur[0]
		y = get_cur[1]
		d = get_cur[2]
		g = get_cur[3]

		d_his=[]
		for gen_idx in range(g+1):
			if gen_idx == 0:
				new_x = x + dydy[d][0]
				new_y = y + dydy[d][1]
				d_his.append(d)
				#dic_matrix[(x,y),(new_x,new_y)]=1
				new_dic_matrix[(x,y)] = 1
				new_dic_matrix[(new_x,new_y)] = 1
				x = new_x
				y = new_y
			else:
				d_len = len(d_his)
				now_d_his = []
				for idx in range(d_len):
					#print("d_his",d_his)
					#print("(d_his[-(idx+1)]",d_his[-(idx+1)])
					now_d = (d_his[-(idx+1)] + 1)%4
					new_x = x + dydy[now_d][0]
					new_y = y + dydy[now_d][1]
					now_d_his.append(now_d)
					#dic_matrix[(x,y),(new_x,new_y)]=1
					new_dic_matrix[(x,y)] = 1
					new_dic_matrix[(new_x,new_y)] = 1	
					x = new_x
					y = new_y
				d_his = d_his + now_d_his


N = int(sys.stdin.readline())
dra_cur = []
for idx in range(N):
	tmp = list(map(int, sys.stdin.readline().split()))
	dra_cur.append(tmp)
plot_cur(dra_cur)
cnt_squ()
