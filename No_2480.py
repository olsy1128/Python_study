a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a == b == c :  # a, b, c 모두 같을때
    price = 10000 + a * 1000 
elif a == b != c: # a, b 같을때
    price = 1000 + a * 100
elif a == c != b: # a, c 같을때
    price = 1000 + a * 100
elif b == c != a: # b, c 같을때
    price = 1000 + b * 100
elif a != b != c : # 모두 다를때
    # 가장 큰 수 판별
    if a > b and a > c : # a가 젤 큼
        price = a * 100
    elif b > c and b > a : # b가 젤 큼
        price = b * 100 
    elif c > a and c > b : # c가 젤 큼
        price = c * 100
        
print(price)