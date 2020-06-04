import sys
dxdy = [[1,-1],[1,1],[-1,1],[-1,-1]]

def bfs():
    global now_idx,now_idy, min_x,min_y,max_x, max_y
    new_matrix = [[0 for col in range(N+1)]for row in range(N+1)]
    new_x = now_idx
    new_y = now_idy

    new_matrix[new_x][new_y] = 5

    for ind in range(1,N):
        if new_x-ind <= 0:
            break
        for idy in range(N):
            if new_y-idy <= 0:
                break
            new_matrix[new_x-ind][new_y-idy] = 1

    for d1_1 in range(d1):
        for idy in range(1,N):
             if new_y-idy <= 0:
                 break
             new_matrix[new_x][new_y-idy] = 1
        new_x = new_x + dxdy[0][0]
        new_y = new_y + dxdy[0][1]
        new_matrix[new_x][new_y] = 5

    

    for d2_1 in range(d2):
        for idy in range(1,N):
             if new_y-idy <= 0:
                 break
             new_matrix[new_x][new_y-idy] = 3

        new_x = new_x + dxdy[1][0]
        new_y = new_y + dxdy[1][1]
        new_matrix[new_x][new_y] = 5

    for idy in range(1,N):
             if new_y-idy <= 0:
                 break
             new_matrix[new_x][new_y-idy] = 3

    for idx in range(1,N):
        if new_x+idx>N:
            break
        for idy in range(1,N):
            if new_y-idy <= 0:
                break
            new_matrix[new_x+idx][new_y-idy] = 3
        for idy in range(N):
            if new_y+idy > N:
                break
            new_matrix[new_x+idx][new_y+idy] = 4

    for d1_2 in range(d1):
        for idx in range(1,N):
            if new_y+idx > N:
                break
            new_matrix[new_x][new_y+idx] = 4
            
        new_x = new_x + dxdy[2][0]
        new_y = new_y + dxdy[2][1]
        new_matrix[new_x][new_y] = 5
        
    for idx in range(1,N):
        if new_y+idx > N:
            break
        for idy in range(N):
            if new_x - idy <=0:
                break
            new_matrix[new_x - idy][new_y+idx] = 2

    for d2_2 in range(d2):
        for idx in range(1,N):
            if new_x - idx <= 0:
                break
            new_matrix[new_x - idx][new_y] = 2
        new_x = new_x + dxdy[3][0]
        new_y = new_y + dxdy[3][1]
        new_matrix[new_x][new_y] = 5
       
    for idx in range(1,N):
        if new_x - idx <= 0 :
            break
        new_matrix[new_x - idx][new_y] = 1
    #for get_matrix in new_matrix:
    #    print(get_matrix)
    return new_matrix


N = int(sys.stdin.readline())

matrix = [[0 for col in range(N+1)]for row in range(N+1)]

for idy in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    for idx, val in enumerate(tmp):
        matrix[idy+1][idx+1] = val

#print(matrix)

min_dif = 1000000


#get x,y d1,d2
for now_idx in range(1,N+1):
    for now_idy in range(1,N+1):
        for d1 in range(1, N):
            for d2 in range(1,N):
                if d1 < 1 or d2 < 1 or (now_idx+d1+d2)>N or (now_idy-d1) >= now_idy or now_idy >= (now_idy+d2) or (now_idy+d2) > N or (now_idy-d1)<1:
                    continue

                new_matrix = bfs()
                dict_cnt = {1:0,2:0,3:0,4:0,5:0}
                
                for now_r in range(1,N+1):
                    for now_c in range(1,N+1):
                        
                        if new_matrix[now_r][now_c] == 5 or new_matrix[now_r][now_c] == 0:
                            dict_cnt[5] = dict_cnt[5] + matrix[now_r][now_c]
                        elif new_matrix[now_r][now_c] == 1:
                            dict_cnt[1] = dict_cnt[1] + matrix[now_r][now_c]
                        elif new_matrix[now_r][now_c] == 2:
                            dict_cnt[2] = dict_cnt[2] + matrix[now_r][now_c]
                        elif new_matrix[now_r][now_c] == 3:
                            dict_cnt[3] = dict_cnt[3] + matrix[now_r][now_c]
                        elif new_matrix[now_r][now_c] == 4:
                            dict_cnt[4] = dict_cnt[4] + matrix[now_r][now_c]    
                
                sort_dic = sorted(dict_cnt.items(), key = lambda x : x[1])

                diff = sort_dic[-1][1] - sort_dic[0][1]
                '''
                if diff == 38:
                    print(now_idx,now_idy, d1,d2)
                    for get_matrix in new_matrix:
                        print(get_matrix)  
                    print(sort_dic,diff)
                '''

                if min_dif > diff:
                    min_dif = diff

print(min_dif)