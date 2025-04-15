#solution for problem 2 (Elevate Box)
n=int(input()) #size of array
a=list(map(int,input().split())) #reading input array
def bal_sum(a,l,i): #function to calculate left and right sum
    sum=0
    if i==0 and l==True or l==False and i==n-1:
        return 0
    else:
        if l==True:
            for j in range(i):
                sum=sum+a[j]
        else:
            for j in range(i+1,n,1):
                sum=sum+a[j]
                
    return sum
for i in range(n): #calculating each elements balanced weight using bal_sum() method
    left=bal_sum(a,True,i)
    right=bal_sum(a,False,i)
    print(abs(left-right),end=' ')
    
