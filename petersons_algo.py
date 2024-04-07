class PetersonMutex:

    def __init__(self):
        self.flag = [False, False] # Flags for each thread
        self.turn = 0 # Indicates whose turn it is
  
    def lock(self, thread_id):
        other_thread = 1 - thread_id # ID of the other thread
        self.flag[thread_id] = True # Indicate interest in entering critical section
        self.turn = thread_id # Set it to our turn
    
      # Wait while the other thread is interested and it's its turn
        while self.flag[other_thread] and self.turn == thread_id:
          pass
  
    def unlock(self, thread_id):
        self.flag[thread_id] = False # Reset flag for the current thread


# Example usage:
import threading
import time
mutex = PetersonMutex()
shared_variable = 0

    def thread_function(thread_id):
        global shared_variable
        for _ in range(5): # Perform some operations
            mutex.lock(thread_id)
            shared_variable += 1 # Critical section
            print(f"Thread {thread_id} - Shared variable: {shared_variable}")
            mutex.unlock(thread_id)
            time.sleep(0.1) # Simulate some work

# Create two threads
thread1 = threading.Thread(target=thread_function, args=(0,))
thread2 = threading.Thread(target=thread_function, args=(1,))
# Start threads
thread1.start()
thread2.start()
# Wait for threads to finish
thread1.join()
thread2.join()
print("Execution completed.")
