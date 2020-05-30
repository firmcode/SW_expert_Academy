import time

list_check  = []
dic_check = {}
N=2500


for idy in range(N):
	for idx in range(N):
		list_check.append([idy,idx])
st=time.time()  

if [2400,2400] in list_check:
	print("in list")
en=time.time()  
print("list time ",en-st)


for idy in range(N):
	for idx in range(N):
		dic_check[idy,idx] = 1
st=time.time()

if (2400,2400) in dic_check:
	print("in dic")

en=time.time()  
print("dic time ",en-st)


vist_list = [[0 for row in range(N)] for col in range(N)]
for idy in range(N):
	for idx in range(N):
		vist_list[idy][idx] = 1
st=time.time()

if vist_list[2400][2400] == 1:
	print("in list")

en=time.time()  
print("list time ",en-st)
