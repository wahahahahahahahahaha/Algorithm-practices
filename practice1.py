n, m = map(int,input().split())
nums=list(map(int, input().split()))

seen={}
result=[]
for i in range(n):
    if m-nums[i] in seen:
        result.append(seen[m-nums[i]])
        result.append(i)
        break

    seen[nums[i]]=i
    

if result:
    print(result[0], result[1])