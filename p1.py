# t denotes number of test cases the user want to test ,it can be taken as integer
t=int(input())
 #take the input as array size and array integers upto t testcases
for i in range(t):
    #variable to count numbers of operations needed to make mininum number as maximum number
    count=0  
    #size of the input array
    n=int(input()) 
    #input array separated by space
    x=list(map(int,input().split()))
    # method min()  to find minimum number in the array
    m=min(x) 
    #iterate the list or array upto n times
    for j in x:
    #check the element in array is greater than minimum element 
        if j>m:
        #if element is greater increment the count
            count=count+1
    print(count)
            
