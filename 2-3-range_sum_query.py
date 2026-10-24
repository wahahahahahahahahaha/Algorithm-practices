n,q=map(int,input().split())
nums=list(map(int, input().split()))

answers = []

# for i in range(q):
#     answers.append(0)
#     l,r=map(int, input().split())
#     for j in range(l-1,r):
#         answers[i]+=nums[j]

# for i in range(q):
#     print(answers[i])

prefix=[]
for i in range(n+1):
    if i==0:
        prefix.append(0)
    else:
        prefix.append(prefix[i-1]+nums[i-1])
### 优化版本
# prefix=[0]*(n+1)
# for i in range(1,n+1):
#     prefix[i]=prefix[i-1]+nums[i-1]


for i in range(q):
    l,r =map(int, input().split())
    answers.append(prefix[r]-prefix[l-1])

for i in range(q):
    print(answers[i])

