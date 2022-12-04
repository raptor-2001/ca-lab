Q3 a--> 
	No, gprof profilling can't decide the sequence of execution of function. It only tells execution time of the a particualr function and number of times it has been called.

Q3 b--> 
	For the given algorithm the complexity depends on the inital arrangement of elements and the element which is being selected as the pivot.
	Time Complexity of conquer part = Time complexity of sorting the left subarray + Time complexity of sorting the right subarray.
	
	Best Case: 
	If the partition element which is selected as the pivot is always the middle element, hence the pivot will always divide the array in two equal parts. T.C = T(n/2) + T(n/2) = 2*T(n/2) finally making the  time complexity O(n*(logn)). Which is the average case.
	
	Worst Case: 
	But, if the partition element which is selected is the smallest or greatest element and the array will be sorted in increasing or decreasing order than in each iteration the element will compared with other elements n times making the time complexity O(n^2), which is worst case.


Gprof Setup and Usage:
 Compile your code with the option -pg (which denotes, requesting the profiler to perform profiling on this code.)
 Run the program in a normal way. When program terminates, a file named gmon.out(Profile data) is generated.
 Now use gprof profile to process profiler data(gmon.out) and produce analysis and statistics of program.
 
Commands -> g++ -Wall -pg main.cpp -o main, ./main, gprof ./main > output

The contents of output are divided into 
	Flat Profile.
	Call Graph.
