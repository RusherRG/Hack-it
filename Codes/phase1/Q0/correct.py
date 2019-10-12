n,m,r = map(int,input().split());
buy=list(map(int,input().split())) #n inputs
sell=list(map(int,input().split())) #m inputs

x = min(buy)
y = max(sell)

if x<=y:
  num = r//x
  c = num*x
  e = num*y
  r = r-c+e

print(r)