# most_frequent_element

n = int(input())
nums = list(map(int, input().split()))

quatity={}

for x in nums:
    quatity[x]=quatity.get(x,0)+1

max_value=None
min_key=None

for key in quatity:
    if max_value is None or quatity[key]>max_value:
        max_value=quatity[key]
        min_key=key
    elif max_value==quatity[key] and key<min_key:
        min_key=key

print(min_key, max_value)
