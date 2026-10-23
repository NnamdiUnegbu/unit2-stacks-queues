# unit2-stacks-queues
CMSC 315 Unit 2 discussion: Python stacks and queues
# Overview
In this assignment, two basic linear data structures in python, stack (LIFO) and Queue (FIFO) were explored. I created and described both and illustrated their characteristics with practical examples.
## Learning Objectives
The assignment involved tackling the following objectives:
•	Implemented stack operations.
•	Implemented queue operations.
•	Implemented LIFO and FIFO operation.
•	Tested edge cases of empty and single item structures.
•	Used data structures in real world situations.
## Stack Implementation
I have implemented Stack class by Python list. The push() operation pushed an element onto the top of the stack and the pop() operation removed and returned the most recently inserted item. The peek() method was used to view the top value without removing it and is_empty() was used to check the stack for values.
The method returned None for an empty stack.Returned None for pop( ) or peek( ) on empty stack.
## Queue Implementation
I used Python's collections.deque to create the Queue class. The enqueue() method was added to the back of the queue; the dequeue() method was added to get and remove the value at the front. The front() function looked at the next value without removing it, is_empty() determined if there was a value in the queue.
method returned None if called with dequeue() or front() on an empty queue.
## Real-World Scenarios
The stack was a model of the history of actions performed on the text. The last editing operation is reversed first, showing LIFO operation.
This line of people was a model of people waiting in line at a café. Customers were served as 'first in, first out' which meant that those waiting in line were served in the order that they came in.
## Test and Edge Cases
I executed the python program and checked the following behaviors:
•	There were four undo operations, which were undone in the reverse order.
•	The first four customers were served in the following order
•	Empty-stack operations returned None.
•	Empty-queue operations returned None.
•	One of the stacks is empty due to the removal of the item.
•	One-Item Queue: An empty queue is created after the removal of its item.
The program exited with a success code (0).
## Memory Usage and Efficiency
As the number of items in the structures increased, the space needed to store them was linear, n, for both structures. The stack was implemented with a Python list, and the queue was implemented using collections.deque, which was used to facilitate pop from the front.
## Discussion Board Reflection
In working on this assignment, I gained insight into the use of stacks and queues to organize data and the order in which it is processed, and how these have implications for real-world applications. Used a python list to represent the stack and collections.deque to represent the queue. I also experimented with writing techniques for adding, removing, viewing and verifying elements in each structure.
One problem I faced was having to deal with empty structures. To overcome this I returned None if pop, peek, dequeue or front was called when there was no item available. I tested these cases and found both of these structure became empty upon removal of one of their elements.
The difference between Stacks and Queues is in the order of removal from the stacks and queues. A stack is Last In, First Out (LIFO) which is appropriate for a text editor's undo buffer as the latest action should be undone first. A queue is First In First Out (FIFO), appropriate for a coffee shop as the customers are served in the same order they arrive. These examples have given me a better understanding of the use of proper data structure to ensure predictable and reliable behavior of the software.
