"""
一、题目描述
给定一个长度为 \(n\) 的非负整数数组 nums 和一个非负整数 \(k\)。

请找出一个连续子数组，使得其中所有元素之和不超过 \(k\)，并输出满足条件的最长连续子数组长度。

如果不存在满足条件的非空连续子数组，输出 0。

注意：连续子数组中的元素必须在原数组中相邻，不能跳过任何元素。
二、输入格式
第一行输入两个整数 \(n,k\)，分别表示数组长度和目标上限。

第二行输入 \(n\) 个非负整数，表示数组元素。
三、输出格式
输出一个整数，表示满足条件的最长连续子数组长度。
四、数据范围
- \(1\le n\le 10^5\)
- \(0\le k\le10^9\)
- \(0\le nums[i]\le10^4\)
"""

### 利用滑动窗口求解
n, k=map(int, input().split())
nums=list(map(int, input().split()))

left=0
right=0
current_sum=0
max_num=0

for right in range(n):
    current_sum+=nums[right]
    while current_sum>k:
        current_sum-=nums[left]
        left+=1
    max_num=max(max_num, right-left+1)

print(max_num)
