# Peterson's Algorithm for Mutual Exclusion

This code implements Peterson's algorithm for mutual exclusion, which allows only one thread to execute its critical section at a time. The algorithm provides a simple and efficient solution to the critical section problem in concurrent programming.

## Topics:

- Peterson's Algorithm Overview
- Implementation of PetersonMutex Class
- Locking Mechanism
- Unlocking Mechanism
- Example Usage and Thread Function
- Multi-Threading Setup
- Execution and Output

## Note:

- Peterson's algorithm is a classic solution to the mutual exclusion problem, ensuring that only one thread accesses a shared resource at a time.
- The PetersonMutex class provides a simple implementation of the algorithm using two flags and a turn variable.
- The lock method is used to acquire the lock before entering the critical section, and the unlock method is used to release the lock after exiting the critical section.
- The example demonstrates the usage of the PetersonMutex class in a multi-threaded environment with two threads.
- Each thread executes a critical section while respecting the mutual exclusion enforced by Peterson's algorithm


