# using python
# i like python
# * l*k* python 

# s=input('enter a sentence')
# v='aeiouAEIOU'
# res=""
# for i in s:
#     if i in v:
#         res+='*'
#     else:
#         res+=i
# print(res)

# ===========================

# check string is palindrom or not 
# s=input()
# if s==s[::-1]:
#     print('pal')
# else:
#     print('not pal')

# ===================================================

# import random 
# jackpot=random.randint(1,20)
# user_num=int(input('enter the number'))
# c=1
# while jackpot!=user_num:
#     if user_num<jackpot:
#         print('choose the higher!!!!')
#     else:
#         print('choose the lower!!!!')
#     user_num=int(input('enter the number'))
#     c+=1
# else:
#     print('you won the game and your jackpot number is',user_num)
#     print('your attempt',c)

l1=[1,2,3,4,5,]
l2=[6,7,8,9,10]
# [7,9,11,13,15]
result = list(map(lambda x, y: x + y, l1, l2))

print(result)

l=['php','python','java','c++']
#with one start with p
result = list(filter(lambda x: x.startswith('p'), l))

print(result)

l=[1,2,3,4,5,6,7,8,9,10]
#square of every number
result = list(map(lambda x: x**2, l))

print(result)

l=[1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x % 2 == 0, l))

print(result) 


#sum of all numer
from functools import reduce
u =reduce(lambda x,y:x+y,l)
print(u)