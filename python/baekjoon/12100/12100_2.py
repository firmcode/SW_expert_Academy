from copy import deepcopy
def move(n, A, flag):
    a = deepcopy(A)
    if flag == 0: #UP
        d = -1
        check = [[False] * n for _ in range(n)]
        for c in range(n):
            for r in range(n):
                if a[r][c] != 0:
                    while 0 <= r + d < n:
                        if a[r + d][c] == a[r][c] and not check[r + d][c] and not check[r][c]:
                            a[r + d][c] *= 2
                            check[r + d][c] = True
                            a[r][c] = 0
                            break
                        else:
                            if a[r + d][c] == 0:
                                a[r + d][c] = a[r][c]
                                a[r][c] = 0
                        r += d
 
    elif flag == 1: #DOWN
        d = 1
        check = [[False] * n for _ in range(n)]
        for c in range(n):
            for r in range(n - 1, -1, -1):
                if a[r][c] != 0:
                    while 0 <= r + d < n:
                        if a[r + d][c] == a[r][c] and not check[r + d][c] and not check[r][c]:
                            a[r + d][c] *= 2
                            check[r + d][c] = True
                            a[r][c] = 0
                            break
                        else:
                            if a[r + d][c] == 0:
                                a[r + d][c] = a[r][c]
                                a[r][c] = 0
                        r += d
 
    elif flag == 2: #LEFT
        d = -1
        check = [[False] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if a[r][c] != 0:
                    while 0 <= c + d < n:
                        if a[r][c] == a[r][c + d] and not check[r][c + d] and not check[r][c]:
                            a[r][c + d] *= 2
                            check[r][c + d] = True
                            a[r][c] = 0
                            break
                        else:
                            if a[r][c + d] == 0:
                                a[r][c + d] = a[r][c]
                                a[r][c] = 0
                        c += d
                        
    elif flag == 3: #RIGHT
        d = 1
        check = [[False] * n for _ in range(n)]
        for r in range(n):
            for c in range(n - 1, -1, -1):
                if a[r][c] != 0:
                    while 0 <= c + d < n:
                        if a[r][c] == a[r][c + d] and not check[r][c + d] and not check[r][c]:
                            a[r][c + d] *= 2
                            check[r][c + d] = True
                            a[r][c] = 0
                            break
                        else:
                            if a[r][c + d] == 0:
                                a[r][c + d] = a[r][c]
                                a[r][c] = 0
                        c += d
    return a
 
def recur(depth, a):
    global trial, max_val, n
    if depth == trial:
        max_val = max(max_val, max(max(k) for k in a))
        return
    for i in range(4):
        recur(depth+1, move(n, a, i))
 
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
trial = 5
max_val = 0
recur(0,a)
print(max_val)
