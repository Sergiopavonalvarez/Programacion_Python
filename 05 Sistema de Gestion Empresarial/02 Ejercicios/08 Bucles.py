

n=5

a=n
print("Primer bucle ")
while a>=0:
    print(a*a)
    a=a-1

b=0
print("Segundo bucle ")
while a<=0:
    print(a*a)
    a=a+1

c=n+1
print("Tercer bucle ")
while c>0:
    c=c-1
    print(c*c)

d=0
e=n
print("Cuatro bucle ")
while d<=e:
    print((e-d)*(e-d))
    d=d+1


print("Quinto bucle")
for f in range(n):
    print(f*f)

print("Sexto bucle")
for g in range(n):
    print((n-g)*(n-g))