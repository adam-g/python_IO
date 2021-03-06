from Queue import Queue
import threading
import time
import random

# List to sort
#unsorted_list = random.sample(xrange(100000), 100000)
unsorted_list = [7, 2, 4, 0, 6, 9, 
                8, 1, 3, 5, 8, 6, 
                3, 5, 0, 6, 4, 1, 
                4, 7, 3, 8, 1, 0, 
                9, 8, 7, 3, 5, 1, 
                5, 6, 7, 5, 4]

list_lock = threading.Lock()

def thread():
    #while not q.empty():
    while threading.active_count() > 1:
        quicksort_helper(unsorted_list, q.get())
        q.task_done()

def quicksort(list):
    quicksort_helper(list, 0, len(list) - 1)

def quicksort_helper(list, tuple):
    first = tuple[0]
    last = tuple[1]

    if first < last:
        split = sort_partition(list, first, last)

        q.put([first, split - 1])
        q.put([split + 1, last])
        
        #quicksort_helper(list, first, split - 1)
        #quicksort_helper(list, split + 1, last)

# Sort a partition where the pivot value is always the first in the list
def sort_partition(list, first, last):
    
    pivot_value = list[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and list[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and list[right_mark] >= pivot_value:
            right_mark -= 1
        if left_mark >= right_mark:
            done = True
        else:
            with list_lock:
                temp = list[left_mark]
                list[left_mark] = list[right_mark]
                list[right_mark] = temp
    
    with list_lock:
        temp = list[first]
        list[first] = list[right_mark]
        list[right_mark] = temp

    return right_mark


def test(list):
    list[0] = 15

q = Queue()
q.put([0,len(unsorted_list) - 1])
thread_time_start = time.time()
for x in range(10):
    t = threading.Thread(target = thread)
    # The thread t will die when the main thread dies if
    # t.daemon is set to True (False by default)
    t.daemon = True
    t.start()
thread_time_stop = time.time()

start_time = time.time()
q.join()    
#quicksort(unsorted_list)
print('Tid att skapa traodar: ', (thread_time_stop - thread_time_start), ' ms')
print('Beraekningstid: ', (time.time() - start_time)*1000, 'ms')
print(unsorted_list)
