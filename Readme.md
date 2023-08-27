# Coding Interview Preparation

## This directory contains all of my assignments from the Coursera's Course: [Coding-Interview-Preparation](https://www.coursera.org/learn/coding-interview-preparation)


## Notes:

__optimizing your code:__
- To optimize space complexity, you may opt for a solution that does in-place changes over creating a new data structure to house the result
- Avoid excessive compiler calls. If you are searching for a value in an array, terminate the loop when the item is found. 
- Modularize this code into a function that is callable repeatedly and reuse the code when possible.
- If there are portions of your code that are no longer required as a result of modularizing, or as a result of an avenue of thought that was not completed, remove it

### deal with technical question:
__STAR method:__
- Situation: project and challenges you faced (the context)
- Task: your responsibilities and assignments
- Action: what you did to solve the problem
- Result: the outcome of your actions

__MEMORY:__
- CPU(Central unit processing) is the brain of the computer. It is responsible for executing instructions and processing data. It is the most important component of a computer system.
- Cache memory is a small amount of memory that is a part of the CPU. It is used to store frequently accessed data and instructions to speed up the processing. Most expensive form, fastest and closest to the CPU.
- Main memory consists of read/random access memory, RAM and read only memory, ROM.

When the CPU receives an instruction to process some information, it first checks the cache to see if the information is here. If the information is available in the cache, it is processed, if it fails to find the required information here, the information is not processed. The CPU then queries the larger, slower main memory then loads this information into the cache for processing.

ROM is busiest when the computer starts and information on the required application is loaded. RAM is programmable, it can retain new information and instructions. RAM holds the current data and instructions that are in current use. The amount of RAM your computer has is directly correlated to how fast it can go. This is because of the transfer rate. Large amounts of RAM mean that the system does not need to transfer information constantly. Instead it can hold and run a number of applications at once using RAM. All the memory needed to operate these applications needs to be available from your RAM. Having too many programs open will affect the performance of your system by exhausting your RAM memory.

- Secondary memory relates to external memory that can be plugged in externally and used to increase the storage capacity of your system.   Accessing this type of memory is slower and requires transferring all required information and instructions into RAM. Examples of secondary memory include hard drives, USB drives, and CDs.
- RAM is volatile memory, meaning that it is lost when the computer is turned off.
- Secondary memory is non-volatile, meaning that it is retained when the computer is turned off.

__Binary:__  
<img src="./Assets/binary_Picture-1.png">
<img src="./Assets/binary_Picture-2.png">

### Basic data structures
<img src="./Assets/data-structures.png">

__Lists and sets:__  

__Lists:__
In most programming languages, lists are represented as objects. This means that in addition to storing data, they also have their own in-built methods. These methods can be used to manipulate the data stored in the list. e.g. append, insert, remove, pop, sort, reverse, index, count, extend, copy, clear. 

it can be `array` or `linked list.`. With `array` you can access any element in the list in constant time(O(1)). `linked list` is a data structure that consists of a sequence of nodes. Each node is composed of two elements: `data` and `poiter`: a reference to the next node in the sequence. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that the head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference. A linked list is a dynamic data structure. The number of nodes in a list is not fixed and can grow and shrink on demand. Any application which has to deal with an unknown number of objects will need to use a linked list.

__Sets:__
A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed). However, the set itself is mutable. We can add or remove items from it. Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

its fast to search cuz it uses `hash function` O(1). Hash function is any function that can be used to map data of arbitrary size to fixed-size values.

__stacks and queues:__  
Stacks and queues are two data structures that are used to store data in a particular order. The main difference between a stack and a queue is that a stack is a LIFO structure (last in, first out), while a queue is a FIFO structure (first in, first out).

Some of the methods that are used to manipulate stacks and queues are: push, pop, peek, enqueue, dequeue, isEmpty, isFull.

__trees:__  
A tree is a data structure that consists of nodes connected by edges. Each node has a parent node and zero or more children nodes. The topmost node in the tree is called the root of the tree. The height of a tree is the length of the longest path to a leaf. The depth of a node is the length of the path to its root. A tree is a recursive data structure. A tree is a recursive data structure because a tree can be defined as a collection of nodes (starting at a root node), where each node is a data structure consisting of a value, together with a list of references to nodes (the "children"), with the constraints that no reference is duplicated, and none points to the root.

Some types of trees are: `binary tree`, `binary search tree`, `AVL tree`, red-black tree, B-tree, B+ tree, splay tree, treap, trie, radix tree, suffix tree, segment tree, k-d tree, k-ary tree, n-ary tree, and more.

searching a tree: DFS( Depth-first search) and BFS(Breadth-first search).

A binary tree has the following properties: 

1. Every node has a maximum of two child nodes.
2. Every node must have a key so that it can be easily identified.
3. Values found to be less than the node are placed in the left child node, and values that are greater are placed in the right child node.


__Hash tables:__  
A hash table is a data structure that maps keys to values for highly efficient lookup. There are two main components of a hash table: an array and a hash function. The array is used to store the data elements, while the hash function is used to convert the key into an array index. The hash function is designed to return the index of the array element where the value should be stored. Hash tables are used to implement `map` and `sets` data structures in many common programming languages.
Some hash algorithms are: `MD5`, `SHA-1`, `SHA-2`, `SHA-3`, ...

`HashMap` allows one null key and multiple null values whereas Hashtable doesn't allow any null key or value. HashMap is generally preferred over HashTable if thread synchronization is not needed.

`synchronization` is the capability to control the access of `multiple threads` to any shared resource at the same time. Without synchronization, it is possible for one thread to modify a shared object while another thread is in the process of using or updating that object's value. This often leads to significant errors.

__Heaps:__  
A heap is a tree-based data structure in which all the nodes of the tree are in a specific order. There can be two types of heaps: `max heap` or `min heap`. In a max heap, the key present at the root node must be the greatest among all the keys present at all of the nodes of the tree. The same rule must be recursively true for all sub-trees in that Binary Tree. The node at the top of the heap with no parents is called the root node. The heap is always a complete binary tree. A complete binary tree is a binary tree in which all the levels of the tree are fully filled, except possibly the last level. To build a heap, we can use an array. The root element will be at Arr[0]. Below table shows indexes of other nodes for the ith node, i.e., Arr[i]:

<img src="./Assets/heap-1.png" >

img above is a binary tree

<img src="./Assets/heap-2.png" >

some methods that are used to manipulate heaps are: `insert`, `delete`, `extractMax`, `extractMin`, `getMax`, `getMin`, `heapify`, `heapSort`.

The main difference between a heap and a binary search tree is that the heap is designed to optimize the retrieval of the maximum or minimum element in the tree, while a binary search tree is designed to optimize searching a particular element in the tree.

__Graphs:__  
A graph is a data structure that consists of a finite set of nodes (or vertices) and a set of edges connecting these nodes. A pair (x,y) is referred to as an edge, which communicates that the x vertex connects to the y vertex. The set of edges describes the connectivity of the graph. A graph is a collection of vertices and edges. A graph is represented using a set of vertices, V, and a set of edges, E. Each edge is a pair (v,w) where v,w ∈ V. The pair is ordered when the graph is directed, and unordered when the graph is undirected. A graph can be represented using an adjacency matrix or an adjacency list.

-> shortest path: Dijkstra's algorithm, Bellman-Ford algorithm, Floyd-Warshall algorithm, Johnson's algorithm, A* search algorithm, breadth-first search, depth-first search, ...

<img src="./Assets/graph-1.png">

__sorting algorithms:__  
8 classical sorting algorithms: bubble sort, insertion sort, selection sort, shell sort, heap sort, merge sort, quick sort, counting sort.
Efficient sorts: heapsort, quicksort, merge sort,..

Reference:

[8 Classical Sorting Algorithms](https://wenfeng-gao.github.io/post/8-classical-sorting-algorithms/)

[Sorting Algorithms in medium](https://medium.com/@bill.shantang/8-classical-sorting-algorithms-d048eec3fdab)

__searching algorithms:__  
Linear search, binary search, jump search, interpolation search, exponential search, Fibonacci search, ...

__devide and conquer:__  
There are two main steps in the divide and conquer approach:
- Divide the problem into a number of subproblems(segments) that are smaller instances of the same problem.
- Conquer the subproblems by solving them recursively. If they are small enough, solve the subproblems as base cases.
- Combine the solutions to the subproblems into the solution for the original problem.(optional)
Benefits of divide and conquer:
+ parallelism: when you have diffrent threads that are working on the same problem ,same time to complete in quicker time, you can divide the problem into subproblems and assign each thread to work on a subproblem. This is called parallelism.

__recursion:__  
there are 3 requirements for implementing a recursive solution
- base case: the condition that stops the recursion
- Diminishing: the condition that makes the problem smaller, bringing it closer to the base case
- Recursive call: the function call that brings the problem closer to the base case

__dynamic programming:__  
`Dynamic programming` is a programming paradigm that promotes solving problems by breaking them into smaller problems and solving these. The solutions are then stored in an appropriate data structure for later use.

`memoization`: The technique of solving sub problems and storing them to save time on a potential future look up

The dynamic programming approach, is commonly applied to combination or optimization problems
ex: knapsack problem, traveling salesman problem, longest common subsequence, longest increasing subsequence, ...

`knapsack problem `is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

__greedy algorithms:__  
`Greedy algorithms` are algorithms that make the locally optimal choice at each step. The choice made by a greedy algorithm may depend on choices made so far, but not on future choices or all the solutions to the subproblem. It iteratively makes one greedy choice after another, reducing each given problem into a smaller one. In other words, a greedy algorithm never reconsiders its choices. This is the main difference from dynamic programming, which is exhaustive and is guaranteed to find the solution. After every stage, dynamic programming makes decisions based on all the decisions made in the previous stage, and may reconsider the previous stage's algorithmic path to solution.

__positional notation:__  
`positional notation` is a numeral system in which the position of a digit in a number determines its value. In the more commonly used decimal positional notation, the value of a digit depends on its position relative to other digits. Each digit is multiplied by an integer power of 10, so that the absolute value of a digit's coefficient is the value of the digit multiplied by the weight of its position. The value of the number is then the sum of the coefficients of each digit multiplied by its respective power of 10.
ex: 123 = 1*10^2 + 2*10^1 + 3*10^0
ex of other positional notation: binary, octal, hexadecimal, ...

__space complexity:__  
 
`space comlexity = input size + auxilary space`

- auxilary space: the space required by the algorithm, not including space taken up by the inputs
- input size: the size of the input
ex: 
```c++
    //Sum Of N Natural Number
    int sum(int n)
    {
     int i,sum=0;
     for(i=n;i>=1;i--)
     sum=sum+i
     return sum;
    }
```
So in the above example input value is 'n' that is constant which will take the space of O(1). Now what about auxiliary space, so it is also O(1) becuase 'i' and 'sum' are also constants. Hence total space complexity is O(1).
Example 2: Sum of all elements in an array
```python
    function sum_of_numbers(arr[],N){
        sum=0
        for(i = 0 to N){
        sum=sum+arr[i]
        }
        print(sum)
    }
```
So here this time there is an algorithm to find the sum of all elements in the array. For that we are passing the array(arr[ ]) and the size of array(N) to the created function. So here,

1. In array(arr) the size of array is "N" and each element will take "4bytes" so the space taken by "arr" will be "N * 4 bytes"
2. "sum" variable stores the sum of all elements and it will take "4 bytes" of space.
3. "i" variable is used to iterate over all the elements in the array and it will also take "4 bytes" of space.
4. Now function call, initialisation of for loop and print function these all comes under the auxiliary space and lets assume these all will take combinely "4 bytes" of space.

Hence, Total space complexity= (4*N + 12)bytes But these 12 bytes((2)+(3)+(4)) are constant so we will not consider it and after removing all the constants(4 from 4*N) we can finally say that this algo have a complexity of "O(N)".


__This course is relevant to multiple Professional Certificates programs. Completing this course will count towards the completion of any of the following programs:__  

[Meta Android Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-android-developer)

[Meta iOS Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-ios-developer)

[Meta Front-End Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-front-end-developer)

[Meta Back-End Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer)

[Meta Database Engineer Professional Certificate](https://www.coursera.org/professional-certificates/meta-database-engineer)