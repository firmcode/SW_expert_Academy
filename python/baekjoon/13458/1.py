import sys  

A = int(sys.stdin.readline())

a_list = list(map(int, sys.stdin.readline().split()))

B, C = map(int, sys.stdin.readline().split())

cnt = 0
for get_a in a_list:
	get_a = get_a - B
	cnt = cnt+1

	if get_a > 0 :
		if get_a > C:
			moc = get_a / C
			#print("moc",moc)
			cnt = cnt + int(moc)
			if (get_a % C) > 0:
				cnt = cnt + 1
		else :
			cnt = cnt+1

	#print(cnt)

print(cnt)