n=int(input().strip())
coordinates=[]
for i in range(n):
    coordinate=list(map(int,input().strip().split()))
    coordinates.append(coordinate)

# x=coordinates[0][0]+coordinates[1][0]+coordinates[2][0]
# y=coordinates[0][1]+coordinates[1][1]+coordinates[2][1]
# z=coordinates[0][2]+coordinates[1][2]+coordinates[2][2]
x=0
y=0
z=0
for coordinate in coordinates:
    x1,y1,z1=coordinate
    x=x+x1
    y=y+y1 
    z=z+z1

if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")