'''
PRN: 2020BTEIT00034
Name: Daulatrao Patil

Quicksort says:
-Partition the list according to a random pivot.
-Quicksort the left half-list.
-Quicksort the right half-list.
So a parallel version comes from the realization that
the two sorts are independent of one another after the
partition:
-Partition the list according to a random pivot.
-Quicksort the two half-lists in parallel.

This is not typical quicksort; it is NlogN in memory
and does not sort the argument lyst as a side effect,
but rather returns a sorted version of the lyst.

Using a shared memory array results in locks.  Even
with the additional memory, there is usually a
reasonable speedup here.

Ref:
http://docs.python.org/library/multiprocessing.html
http://docs.python.org/py3k/library/multiprocessing.html
'''

import random, time, sys
from multiprocessing import Process, Pipe

def main():
    """
    This is the main method, where we:
    -generate a random list.
    -time a sequential quicksort on the list.
    -time a parallel quicksort on the list.
    """
    N = 100000
    if len(sys.argv) > 1:  #the user input a list size.
        N = int(sys.argv[1])

    #We want to sort the same list, so make a backup.
    backup_list = [random.random() for x in range(N)]

    #Sequential quicksort a copy of the list.
    main_list = list(backup_list)            #copy the list
    start_time = time.time()             #start time
    main_list = quicksort(main_list)          #quicksort the list
    elapsed_time = time.time() - start_time   #stop time
    
    if not isSorted(main_list):
        print('quicksort did not sort the lyst. oops.')
        
    print('Sequential quicksort: %f sec' % elapsed_time)

    #So that cpu usage shows a lull.
    time.sleep(3)
    
    #Parallel quicksort.
    main_list = list(backup_list)
    
    start_time = time.time()
    n = 3 #2**(n+1) - 1 processes will be instantiated. I set the number of processes to be high since, with a random choice of pivot, it is unlikely the work will distribute evenly.

    #Instantiate a Pipe so that we can receive the process's response.
    pconn, cconn = Pipe()
    
    #Instantiate a process that executes quicksortParallel on the entire list.
    p = Process(target=quicksortParallel, \
                args=(main_list, cconn, n))
    p.start()
    
    main_list = pconn.recv()
    #Blocks until there is something (the sorted list) to receive.
    
    p.join()
    elapsed_time = time.time() - start_time

    if not isSorted(main_list):
        print('quicksortParallel did not sort the lyst. oops.')

    print('Parallel quicksort: %f sec' % elapsed_time)
    
def quicksort(list_array):
    """
    Quicksort implementation, return a new sorted version of the input list.
    Faster quicksort in that it relies on built-in list comprehensions and concatenation.
    """
    if len(list_array) <= 1:
        return list_array
    pivot = list_array.pop(random.randint(0, len(list_array)-1))
    
    return quicksort([x for x in list_array if x < pivot]) \
           + [pivot] \
           + quicksort([x for x in list_array if x >= pivot])

def quicksortParallel(list_array, conn, procNum):
    """
    Partition the list, then quicksort the left and right sides in parallel.
    """

    if procNum <= 0 or len(list_array) <= 1:
        #In the case of len(lyst) <= 1, quicksort will immediately return anyway.
        conn.send(quicksort(list_array))
        conn.close()
        return

    #Create two independent lists (independent in that elements will never need be compared between lists).
    pivot = list_array.pop(random.randint(0, len(list_array)-1))

    leftSide = [x for x in list_array if x < pivot]
    rightSide = [x for x in list_array if x >= pivot]

    #Creat a Pipe to communicate with the left subprocess
    pconnLeft, cconnLeft = Pipe()
    
    #Create a leftProc that executes quicksortParallel on the left half-list.
    leftProc = Process(target=quicksortParallel, \
                       args=(leftSide, cconnLeft, procNum - 1))
    
    #Again, for the right.
    pconnRight, cconnRight = Pipe()
    rightProc = Process(target=quicksortParallel, \
                       args=(rightSide, cconnRight, procNum - 1))

    #Start the two subprocesses.
    leftProc.start()
    rightProc.start()

    #Our answer is the concatenation of the subprocesses' 
    #answers, with the pivot in between. 
    conn.send(pconnLeft.recv() + [pivot] + pconnRight.recv())
    conn.close()

    #Join our subprocesses.
    leftProc.join()
    rightProc.join()

def isSorted(lyst):
    """
    Return whether the argument lyst is in non-decreasing order.
    """
    for i in range(1, len(lyst)):
        if lyst[i] < lyst[i-1]:
            return False
    return True


#Call the main method if run from the command line.
if __name__ == '__main__':
    main()
    
    
    
