<b>Triangle pattern 1</b><br>
In this challenge, the task is to build a right-angled triangle using integers, where each row contains an increasing number of integers.<br>

<b>Input Format</b> <br>

The first line contains a single integer N, which indicates the height of the triangle. <br>

<b>Output Format</b> <br>

For an input of N, print the right angle triangle asshown in the example. <br>
<b>Code:</b> <br>
n=int(input()) <br>
c=1 <br>
integer=1 <br>
while c<=n: <br>
    for _ in range(1,c+1,1): <br>
        print(integer,end=' ') <br>
        integer=integer+1 <br>
    c=c+1 <br>
    print() <br>


