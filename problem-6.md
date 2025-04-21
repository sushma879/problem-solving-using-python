<pre>Ashok and Kumar recently got into running, and decided to compare how much they ran on different days.

They each ran for N days. On the i-th day, Ashok ran Ai meters and Kumar ran Bi meters.

On each day:

Ashok is unhappy if Kumar ran strictly more than twice his distance, and happy otherwise. Similarly, Kumar is unhappy if Ashok ran strictly more than twice his distance, and happy otherwise. For example:

If Ashok ran 200 meters and Kumar ran 500 meters, Ashok would be unhappy but Kumar would be happy. If Ashok ran 500 meters and Kumar ran 240 meters, Ashok would be happy and Kumar would be unhappy. If Ashok ran 300 meters and Kumar ran 500 meters, both Ashok and Kumar would be happy. You need to determine how many of the N days both Ashok and Kumar were happy.

Input Format

The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three lines of input:
The first line contains a single integer N — the number of days.
The second line contains N space-separated integers A_1, A_2, ..., A_N — the distances run by Ashok on the N days.
The third line contains N space-separated integers B_1, B_2, ..., B_N — the distances run by Kumar on the N days.
  
Output Format

For each test case, output the number of days when both Ashok and Kumar were happy, on a new line. </pre>
<b>Code-</b><br>
<pre>
#Reading number of test cases
t=int(input())
def happy_count(n,a,b): #method to count the number of days both were happy
    count=0
    for i in range(n):
        x=a[i]
        y=b[i]
        if x>2*y or y>2*x : #checking anyones score is more than twice than the score of other
            continue
        else:
            count=count+1
    return count
        
for i in range(t): #taking input upto 't' testcases
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(happy_count(n,a,b))
</pre>
