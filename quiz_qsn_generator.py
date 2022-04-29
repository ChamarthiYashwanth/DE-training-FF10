# name - Chamarthi Yashwanth

# 1. Operators

# list of operators
# 1.arithmetic operators
# 2.logical operators
# 3.bit wise operators
# 4.assignment operators
# 5.comparison operators
# 6.identity operators
# 7.membership operators

import random

d = {'yash':55,'snehith':45,'rahul':50}
name = input()
if name in d.keys(): # membership
    score = d[name]
else:
    d[name] = 0
    score = 0
a = random.randint(1,101)
b = random.randint(1,101)
operators = ['+','-','*','//']
choice = random.choice(operators)
res = str(a)+choice+str(b) # arithmatic
print(res)
while True:
    ans = int(input())
    if ans is eval(res): # identity
        score += 5 # assignment
        d[name] = score
        print('correct answer')
        print('your name:',name)
        print('your current score:',d[name])
        break
    else:
        print('wrong answer try again')
if score <= 20: # comparision
    print('your current level is Beginner')
elif score > 20 and score <= 50:  # logical
    print('your current level is Intermediate')
elif score > 50:
    print('your current level is Pro')

# bitwise operator
a = 2234
b = a>>2 # right shift
print(b)