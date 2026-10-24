n=int(input())
nums=list(map(int, input().split()))

# nums.sort()

quatity={}
for x in nums:
    if x  not in quatity:
        quatity[x]=1
    else:
        quatity[x]+=1 
    # if-else 可用 quatity[x]=quatity.get(x,0)+1 代替
    # quantity.get(x, 0)：如果键 x 存在，就返回它对应的次数。
    # 如果键 x 不存在，就返回默认值 0。

# for key, value in quatity.items():
#     print(key,value)

# 优化后先统计再排序，节省排序时间
for key in sorted(quatity):
    print(key, quatity[key])