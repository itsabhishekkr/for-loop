#print a =2 and b=5
#output
# 1
# 2
# 3
# 4
# 5
a=int(input('a='))
b=int(input("b="))
for i in range(a,b+1,1):
    print(i)
m=int(input())
i=1
while(i<=m):
    print(pow(2,i))
    i=i+1
n=int(input())
i=1
for i in range(1,n+1,1):
    print(pow(2,i))


w=int(input("enter no."))
for i in range(1,w+1,2):
    print(i)

w=int(input("input no."))
for i in range(w,0,-2):
    print(i)

   # print multipal of 3
a=int(input())
b=int(input())
for i in range(a,b+1,1):
    print(3*i)
# number from n to 1
n=int(input())
for i in range(n,0,-1):
    print(i)
#find even number 2 t0 n-1
n =int(input("input"))
c=0
for i in range(2,n+1,1):
    print(i)
    if(i%2==0):
        c=c+1
print(c)
# prime number 
n=int(input("enter number"))
a=False
for d in range(2,n,1):
        print(d)
        if(n%d==0):
                a=True
if(a==True):
         print(" NOT prime")
else:
     print(" prime")  
        
