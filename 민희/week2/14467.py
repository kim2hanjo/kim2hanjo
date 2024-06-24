# 백준 소가 길을 건너간 이유1
N = int(input())
ans = 0
dict = {}

for i in range(N):
    key, value = input().split(' ')

    if key in dict and value != dict[key]:
        ans += 1 
        
    dict[key] = value 
    
print(ans)