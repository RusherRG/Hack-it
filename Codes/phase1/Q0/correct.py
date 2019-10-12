x,y = map(int , input().split())
sub = x-y
if sub % 10 == 9:
    sub = sub-1
else:
    sub = sub+1
print(sub)