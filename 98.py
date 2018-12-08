n=int(raw_input())
a=[]
for i in range(n):
    b=int(raw_input())
    a.append(b)
c=list(a)
c.sort()
for j in range(n):
    if c[n-1]==a[j]:
        print j+1
