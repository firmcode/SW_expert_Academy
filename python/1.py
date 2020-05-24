def solution(n, delivery):
	answer = ''

	deli_dict = {}
	for idx in range(1,n+1):
		deli_dict[idx] = '?'

	for get_list in delivery:
		if get_list[-1] == 1:
			deli_dict[get_list[0]]='O'
			deli_dict[get_list[1]]='O'

	for get_list in delivery:

		if get_list[-1] == 0:
			for key in deli_dict:
				if deli_dict[get_list[0]] == 'O':
					deli_dict[get_list[1]] = 'X'
				if deli_dict[get_list[1]] == 'O':
					deli_dict[get_list[0]] = 'X'

	for val in deli_dict.values():
		answer = answer + val

	return answer

n=7
delivery = [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]
solution(n, delivery)

