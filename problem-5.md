<b>Ram's Absence Streak</b> <br>
Ram has been going to the academy for N days, and his attendance record is represented as an array of 0's and 1's. A 1 means Ram was present that day, and a 0 means Ram was absent. Now, Ram is curious to find out the maximum number of consecutive days he was absent.<br>

<b>Input Format</b> <br>

The first line contains N, the number of days.<br>
The second line contains N integers (either 0 or 1), representing Ram’s attendance record for the N days.<br>

<b>Output Format </b> <br>

Print the maximum number of consecutive days Ram was absent. <br>
<pre>
n=int(input())
l=list(map(int,input().split()))
max=0
for i in range(n):
    c=0
    while (i < n and l[i]==0):
        c=c+1
        i=i+1
    if c>max:
        max=c
print(max)
    </pre>
