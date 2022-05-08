import io
import sys

_INPUT = """\
6
3
3 2 1
2 2 1
1 1 1
3
1
4
9
3
1 1 1
1 1 1
9 9 9
1
4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  D=[list(map(int,input().split())) for _ in range(N)]
  ad=[[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      ad[i][j]+=D[i][j]
      if i>0: ad[i][j]+=ad[i-1][j]
      if j>0: ad[i][j]+=ad[i][j-1]
      if i>0 and j>0: ad[i][j]-=ad[i-1][j-1]
  ans=[0]*(N**2+1)
  for i in range(N):
    for j in range(N):
      for k in range(N-i):
        for l in range(N-j):
          tmp=ad[i+k][j+l]
          if k>0: tmp-=ad[k-1][j+l]
          if l>0: tmp-=ad[i+k][l-1]
          if k>0 and l>0: tmp+=ad[k-1][l-1]
          ans[(i+1)*(j+1)]=max(ans[(i+1)*(j+1)],tmp)
  aans=[0]*(N**2+1)
  for i in range(N**2):
    aans[i+1]=max(aans[i],ans[i+1])
  Q=int(input())
  for i in range(Q):
    print(aans[int(input())])