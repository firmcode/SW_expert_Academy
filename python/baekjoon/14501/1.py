import sys
max_cost = 0
def get_max_val(today,schud,now_cost):
	global max_cost
	if now_cost > max_cost :
		max_cost = now_cost

	for idx, get_ti in enumerate(Ti):
		if idx < today:
			continue
		
		if (today + get_ti) <= day:
			new_day = today + get_ti
			now_cost = now_cost + Pi[idx]
			#print("today",today,"get_ti",idx," ",get_ti)
			get_max_val(new_day,schud,now_cost)
			now_cost = now_cost - Pi[idx]

		today = today+1



day = int(sys.stdin.readline())

Ti = []
Pi = []
for inx in range(day):
	t_tmp, p_tmp = map(int, sys.stdin.readline().split())
	Ti.append(t_tmp)
	Pi.append(p_tmp)


schud = [1 for col in range(day)]
now_cost = 0
get_max_val(0,schud,now_cost)

print(max_cost)



