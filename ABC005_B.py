import io
import sys

_INPUT = """\
6
3
1
2
3
3
3
3
3
5
3
1
4
1
5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  T=[int(input()) for _ in range(N)]
  print(min(T))