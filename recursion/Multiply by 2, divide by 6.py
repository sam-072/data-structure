# Code by : Sam._.072

def Factors(n,l):
    k=2
    while n>1:
        if n%k==0:
            l.append(k)
            n=n//k
        else:
            k+=1
        if k>3:
            return False
    return True
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        l=[]
        if n==1:
            print(0)
        elif Factors(n, l):
            n2,n3=0,0
            for i in l:
                if i==2:
                    n2+=1
                elif i==3:
                    n3+=1
            if n2>n3:
                print(-1)
            elif n2==n3:
                print(n2)
            else:
                print(n3+n3-n2)
        else:
            print(-1)