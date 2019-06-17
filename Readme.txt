Akanksha Mahajan
Student ID : 112074564
Course :  CSE535(Fall 2018) Asynchronous Systems
HomeWork Assignment 2




Info for Solution 1 :
File is assg1_1.da
Credit source : https://github.com/DistAlgo/distalgo/tree/master/da/examples/lamutex/


I have implemented 5 rules of Lamport in this code. I have assumed “any” mentioned in the paper to be delete “any one” request message from the request queue. 


Run command : python -m da assg1_1.da <no_of_processes> <no_of_requests>
At any time there can be multiple requests of process pending in the request queue. 


I have divided the sequential code of orig.da into 3 functions :
One to send message : sendr()
One for Critical Section : 
One to release resource : releaser()


Since we are removing “any one” request message from the queue. So on running the code it can either violate Safety ( 2 processes can be in CS at same time) or liveness (processes can be in deadlock state.


Info for Solution 2 :
File is Solution 2_akanksha_mahajan.pdf. 
In this pdf I have mentioned the scenarios where lamport algorithm can violate safety and liveness.




Info for Solution 3:
Files :
  1. main.da (contains monitor process Log process) : It compares the performance of all algorithms (spec.da, my_mutex.da and orig.da)
2. My_mutex.da : It contains the Lamport modified code as in question 1 where I have divided the sequential flow into three sections. 
3. Spec.da : provided in lamutex/spec.da 
4. Orig.da : original lamport example provided in the class


My  main program is "main.da", and it runs with a command : 
"p" is for number of processes, 
"r" is for total number of requests, 
"n" is for number of runs for correctness testing, and 
"d" and "a" are for number of parameter values and number of repetitions, respectively, for performance testing:


Command :  python.exe -m da main.da p r n d a
*Kill the process if system hangs in deadlock case


Main.da performs two tasks.
1. Correctness :
It calculates the correctness of 3 programs “n” number of times by randomly selecting process number and request number between 1 to p and 1 to n respectively.
If system violates safety then it prints “Safety has been violated as more than one process is there in Critical Section”
Else it prints, “No safety violated”
And In case of deadlock, the system hangs.


1. Performance :
It calculates the performance in two steps:


2.1   It performs “d” different runs on "p" processes and up to "r" requests evenly spaced each request with "a" repetitions for each run for each algorithm


2.2   It performs “d” different runs on "p" processes evenly spaced and  "r" requests with "a" repetitions for each run for each algorithm


It then calculates the average time of 2.1 and 2.2 over r  repetitions and compare all 3 algorithms.


Approach :  
1. In main.da, I have created a Log class which is basically a controller and every process sends a message to this class if they enter CS and when they exit CS. This way Log Class keeps track of number of processes in CS by maintaining a counter.


1. Log process also keeps track of running time of all processes and return average running time of all algorithms over all repetitions 


Conclusion : 
It can easily be checked that most of the time  the running time of
 my_mutex.da < orig.da < specs.da
Specs.da is taking most time to complete all the tasks.