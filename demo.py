# using python
# i like python
# * l*k* python 

s=input('enter a sentence')
v='aeiouAEIOU'
res=""
for i in s:
    if i in v:
        res+='*'
    else:
        res+=i
print(res)

===========================

# check string is palindrom or not 
s=input()
if s==s[::-1]:
    print('pal')
else:
    print('not pal')

===================================================

import random 
jackpot=random.randint(1,20)
user_num=int(input('enter the number'))
c=1
while jackpot!=user_num:
    if user_num<jackpot:
        print('choose the higher!!!!')
    else:
        print('choose the lower!!!!')
    user_num=int(input('enter the number'))
    c+=1
else:
    print('you won the game and your jackpot number is',user_num)
    print('your attempt',c)
             