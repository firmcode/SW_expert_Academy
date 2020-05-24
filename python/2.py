
def solution(id_list, k):
    answer = 0
    
    coupon_dic = {}
    
    for clients in id_list:
        clients_ids = clients.split()
        clients_ids = list(set(clients_ids))
        for get_id in clients_ids: 

            if get_id in coupon_dic:
                if coupon_dic[get_id] >= k:
                    continue
                coupon_dic[get_id] = coupon_dic[get_id] + 1
            else :
                coupon_dic[get_id] = 1
                    
    for val in coupon_dic.values():
        #print(val)
        answer = answer + val
                    
    #print(answer)
    return answer


id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
k = 3 
solution(id_list,k)