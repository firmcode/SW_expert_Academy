def cmp1():
	return (box1[2] == box2[6])
def cmp2():
	return (box2[2] == box3[6])
def cmp3():
	return (box3[2] == box4[6])

def shift_box(box,box_dir):
	if box_dir == 1:
		tmp = box[-1]
		box=box[:-1]
		box = [tmp] + box
	else:
		tmp = box[0]
		box=box[1:]
		box = box + [tmp]
	return box

def sim1(box_dir):
	global box1, box2, box3, box4
	shift = [0,0,0,0,0]
	shift[1] = box_dir

	if cmp1() == False:
		shift[2]= -(box_dir)
		if cmp2()== False:
			shift[3]= (box_dir)
			if cmp3()== False:
				shift[4]= -(box_dir)
	
	if shift[1] != 0:
		box1 = shift_box(box1,shift[1])
	if shift[2] != 0:
		box2 = shift_box(box2,shift[2])
	if shift[3] != 0:
		box3 = shift_box(box3,shift[3])
	if shift[4] != 0:
		box4 = shift_box(box4,shift[4])

def sim2(box_dir):
	global box1, box2, box3, box4
	shift = [0,0,0,0,0]
	shift[2] = box_dir

	if cmp1() == False:
		shift[1]= -(box_dir)
	if cmp2()== False:
		shift[3]= -(box_dir)
		if cmp3()== False:
			shift[4]= (box_dir)
	
	if shift[1] != 0:
		box1 = shift_box(box1,shift[1])
	if shift[2] != 0:
		box2 = shift_box(box2,shift[2])
	if shift[3] != 0:
		box3 = shift_box(box3,shift[3])
	if shift[4] != 0:
		box4 = shift_box(box4,shift[4])

def sim3(box_dir):
	global box1, box2, box3, box4
	shift = [0,0,0,0,0]
	shift[3] = box_dir

	if cmp2()== False:
		shift[2]= -(box_dir)
		if cmp1() == False:
			shift[1]= (box_dir)
	if cmp3()== False:
		shift[4]= -(box_dir)

	if shift[1] != 0:
		box1 = shift_box(box1,shift[1])
	if shift[2] != 0:
		box2 = shift_box(box2,shift[2])
	if shift[3] != 0:
		box3 = shift_box(box3,shift[3])
	if shift[4] != 0:
		box4 = shift_box(box4,shift[4])

def sim4(box_dir):
	global box1, box2, box3, box4
	shift = [0,0,0,0,0]
	shift[4] = box_dir

	if cmp3()== False:
		shift[3]= -(box_dir)
		if cmp2()== False:
			shift[2]= (box_dir)
			if cmp1() == False:
				shift[1]= -(box_dir)

	if shift[1] != 0:
		box1 = shift_box(box1,shift[1])
	if shift[2] != 0:
		box2 = shift_box(box2,shift[2])
	if shift[3] != 0:
		box3 = shift_box(box3,shift[3])
	if shift[4] != 0:
		box4 = shift_box(box4,shift[4])


box1 = [*map(int, input())]
box2 = [*map(int, input())]
box3 = [*map(int, input())]
box4 = [*map(int, input())]
N = int(input())

for idx in range(N):
	select, box_dir = map(int, input().split())
	if select == 1:
		sim1(box_dir)
	elif select == 2:
		sim2(box_dir)
	elif select == 3:
		sim3(box_dir)
	elif select == 4:
		sim4(box_dir)


score = 0
if box1[0] == 1:
	score = score+1
if box2[0] == 1:
	score = score+2
if box3[0] == 1:
	score = score+4
if box4[0] == 1:
	score = score+8


print(score)



