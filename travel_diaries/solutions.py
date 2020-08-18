import sys
def input():
    return sys.stdin.readline()
n,m=map(int,input().split())
lis=[[i for i in input().split()] for j in range(n)]
pos=[];tot=0
for i in range(n):
    for j in range(m):
        if lis[i][j]=='2':
            pos.append((i,j))
        if lis[i][j]=='1':
            tot+=1
from collections import *
X=[-1,1,0,0]
Y=[0,0,-1,1]
vis=defaultdict(int)
lev=0
while(True):
    new=set()
    for i in pos:
        for j in range(4):
            nx=X[j]+i[0]
            ny=Y[j]+i[1]
            if 0<=nx<n and 0<=ny<m and lis[nx][ny]=='1' and vis[(nx,ny)]==0:
                 vis[(nx,ny)]=1
                 new.add((nx,ny))
                 tot-=1
    pos=new
    if len(pos)==0:
        break
    lev+=1
if tot==0:
    print(lev)
else:
    print(-1)
