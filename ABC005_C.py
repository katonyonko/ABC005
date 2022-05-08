import io
import sys

_INPUT = """\
6
1
3
1 2 3
3
2 3 4
1
3
1 2 3
3
2 3 5
1
3
1 2 3
10
1 2 3 4 5 6 7 8 9 10
1
3
1 2 3
3
1 2 2
2
5
1 3 6 10 15
3
4 8 16
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  N=int(input())
  A=list(map(int,input().split()))
  M=int(input())
  B=list(map(int,input().split()))
  ans='yes'
  now=0
  for i in range(M):
    while now<N and A[now]<B[i]-T:
      now+=1
    if now==N or B[i]<A[now]: ans='no'; break
    now+=1
  print(ans)