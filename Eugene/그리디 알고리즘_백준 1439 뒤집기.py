#!/usr/bin/env python
# coding: utf-8

# ## 그리디 알고리즘
# * 현재 상태에서 볼 수 있는 선택지 중에 최선의 선택을 하는 알고리즘입니다.
# * 장단점
# 장점: 우수한 시간복잡도를 가지고 동적계획법보다 구현이 쉽다.
# 단점: 최적의 해를 항상 보장하진 못한다.
# #
# * 핵심원리 3가지
# 1) 현재 상태에서 가장 최선이라고 판단하는 해를 선택한다.
# 2) 현재 선택한 해가 전체 문제의 제약 조건 내에 있는지 판별한다.
# 3) 현재까지 선택한 해의 집합들이 전체적인 문제해결이 가능한지 판별한다. 아닐 경우, 다시 1) 로 돌아가 동일한 과정을 반복수행한다.
# * 사용을 위한 조건
# 1) 어떠한 선택으로 전체 문제의 최적해를 도출이 반드시 되어야 함.
# 2) 전체 문제 내의 거치는 여러 단계 하나 하나에서도 최적해가 나와야함.

# In[3]:


from PIL import Image

image = Image.open("1.png")

image # 알고리즘에서의 최선의 선택 예시


# In[ ]:


s = input() # 입력받을 0,1로 이뤄진 문자열 s

n = int(s[0])# 문자열 첫번째 원소 초기화
#print(n)

answer = [0] * 2 # 0, 1로 이뤄진 집단 갯수를 담을 리스트: answer[0]에는 0 집단 갯수, answer[1]에는 1 집단 갯수
#print(answer)

answer[n] = 1 #첫번째 원소의 숫자 갯수 1로 초기화

for i in s:
    number = int(i)
    if  n == number: 
        continue
    else:
        answer[number] += 1
        n = number
        #print(n)

print(min(answer[0], answer[1]))


# In[ ]:


# 백준 11047번 문제 - 동전 0

"""
각 단계에서 최솟값을 찾을 때까지 내림차순으로 내려가면서 나눈다.
"""

n, k = map(int, input().split())# n: 화폐종류수, k: 나머지 돈(거스름돈)

coin = []

for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)# 내림차순 전환

answer = 0
for c in coin:
    if k >= c:
        answer += k // c
        k %= c
        if k <=0: # 반복문 탈출
            break

print(answer) # 동전의 최솟값


# In[ ]:




