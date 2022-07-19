num_list=[]

for i in range(9):
    num = int(input())
    num_list.append(num)

max_num = num_list[0]

for k in num_list :
    if k > max_num :
        max_num = k
        
print(max_num, num_list.index(max_num)+1)