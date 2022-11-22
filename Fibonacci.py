num = int(input("num = "))

def Fibonacci(a,b=0,c=1):
    if a!=0:
        print(f"{b}",end=" ")
        a-=1
        Fibonacci(a,c,b+c)
Fibonacci(num+2)
