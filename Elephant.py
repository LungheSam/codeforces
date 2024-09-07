from math import ceil
def findSteps(n):
    steps=0
    if n<=5:
        steps=1 
    else :
        steps=ceil(n/5)
    return steps
x=int(input().strip())
print(findSteps(x))