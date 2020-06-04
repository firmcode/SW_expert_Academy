import time
dict_test = {}
for idx in range(100*1000):
	dict_test[idx] = idx

st = time.time()

for key, val in dict_test.items():
	key_tmp = key
	val_tmp = val
ed = time.time()
print("1 : ",ed -st)

st = time.time()

for key in dict_test.keys():
	key_tmp = key
	val_tmp = dict_test[key]
ed = time.time()
print("2 : ",ed -st)