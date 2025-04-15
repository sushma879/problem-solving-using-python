# problem-solving-using-python
Logical questions or problems are solved using python programming language<br>
<b>Problem 1 : Minimum Operations to Make the Smallest to the Largest </b> <br>
You are given an array A of size N.<br>

Let M be the minimum value present in the array initially. In one operation, you can choose an element Ai (1 ≤ i ≤ N) and an integer X (1 ≤ X ≤ 100), and set Ai = X. <br>

Determine the minimum number of operations required to make M the maximum value in the array A <br>
<b>Input Format </b> <br>

The first line of input will contain a single integer T, denoting the number of test cases. Each test case consists of multiple lines of input: The first line of each test case contains a single integer N — the size of the array. The next line of each test case contains N space-separated integers A1, A2, ..., AN — the elements of the array. <br>
<b>CODE - </b> https://github.com/sushma879/problem-solving-using-python/blob/main/p1.py<br> <br>
<b>Problem 2: Elevate box</b> <br>
In a mystical land of computing, there exists a magical device called the ElevateBox. It is known for its unique balancing act where, for every element in an array, it tries to balance the weight on its left side and right side. <br>

You have been tasked with helping the ElevateBox balance an array A of size N. For each position i, the ElevateBox performs the following calculation: <br>

It calculates the total "weight" on its left side, which is the sum of all elements to the left of A[i]. If there are no elements to the left, the weight is considered 0. <br>
It calculates the total "weight" on its right side, which is the sum of all elements to the right of A[i]. If there are no elements to the right, the weight is considered 0. <br>
Once the ElevateBox computes both sums, it tries to measure how unbalanced that position is by calculating: <br>

Your job is to calculate and print the Balance Array B that the ElevateBox generates. <br>
<b>Input Format</b> <br>

The first line contains an integer N — the size of the array A. <br>
The second line contains N integers — the elements of array A. <br>

<b>Output Format</b> <br>

Print the elements of the Balance Array B, separated by spaces, that the ElevateBox has computed. <br>
<b>Code:</b> <br>

