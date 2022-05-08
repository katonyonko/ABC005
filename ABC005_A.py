import io
import sys

_INPUT = """\
6
4 8
4 7
4 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  x,y=map(int,input().split())
  print(y//x)