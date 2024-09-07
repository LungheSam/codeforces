
invites_total=int(input().strip())
invites_numbers=input().strip().split(" ")
invites_numbers=list(map(int,invites_numbers))

output1=[0 for i in range(invites_total)]
for index,value in enumerate(invites_numbers):
    output1[value-1]=index+1
output1=list(map(str,output1))
print(" ".join(output1))
