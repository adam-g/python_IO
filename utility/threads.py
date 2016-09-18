import threading 
from Queue import Queue
import time

# Used as a lock for the print function
# Will have to use a lock for each thing to lock
print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(0.5)
    
    # Only one thread at the time can acquirre the lock,
    # no other thread is allowed to uxecute the code block below
    # while the lock is acquired.
    with print_lock:
        print(threading.current_thread(), worker)

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

q = Queue()

for x in range(10):
    t = threading.Thread(target = threader)
    # The thread t will die when the main thread dies if
    # t.daemon is set to True (False by default)
    t.daemon = True
    t.start()

start_time = time.time()

for worker in range(20):
    q.put(worker)

# Wait until the thread terminates
q.join()

print('Entire work took: ', time.time()-start_time)
