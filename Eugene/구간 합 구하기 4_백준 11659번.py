#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
sec = [0]
tmp = 0

for i in range(n):
    tmp += nums[i]
    sec.append(tmp)
    
for i in range(m):
    a, b = map(int, input().split())
    print(sec[b] - sec[a-1])

