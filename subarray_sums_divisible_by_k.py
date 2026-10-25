"""
一、题目描述
给定一个长度为 \(n\) 的整数数组 nums 和一个正整数 \(k\)。

请你统计数组中有多少个非空连续子数组，满足该子数组所有元素之和能够被 \(k\) 整除。

注意：连续子数组必须由原数组中相邻的元素组成，不能跳过中间元素。不同的起止位置视为不同的子数组。
二、输入格式
第一行输入两个整数 \(n,k\)，分别表示数组长度和除数。

第二行输入 \(n\) 个整数，表示数组元素。
三、输出格式
输出一个整数，表示满足条件的连续子数组数量。
"""

n, k = map(int, input().split())
nums=list(map(int, input().split()))

# 构造前缀和列表
prefix=[0]*(n+1)
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+nums[i-1]

count=0 # 计数器

### o(n*n)
# sums=0 
# for r in range(1,n+1):
#     for l in range(r):
#         sums=prefix[r]-prefix[l]
#         if sums % k == 0:
#             count+=1

seen={0:1}
for i in range(1,n+1):
    remainder = prefix[i]%k

    count+=seen.get(remainder,0)
    seen[remainder]=seen.get(remainder,0)+1

print(count)


### 优化版本 去掉前缀和的使用 空间复杂度由o(n)->o(min(n,k))
# seen = {0: 1}
# count = 0
# current_sum = 0

# for x in nums:
#     # 更新当前累计和
#     current_sum +=x

#     # 计算当前累计和的余数
#     remainder = current_sum % k
#     # 统计满足条件的子数组
#     count +=  seen.get(remainder, 0)
#     # 更新字典
#     seen[remainder] = seen.get(remainder, 0)+1
# print(count)


