x,y = map(int , input().split())
z= x-y
lz = len(str(z))
n =z+1
ne = z-1
ln = len(str(n))
lne = len(str(ne))
if lne < lz:
  print(ne)
elif ln > lz:
    print(n)
elif lne == lz:
    print(n)
elif ln == lz:
    print(ne)
