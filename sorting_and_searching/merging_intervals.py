# Python3 to merge overlapping intervals
# in O(n Log n) time and O(1) extra space
def mergeIntervals(arr):

    # Sorting based on the increasing order
    # of the start intervals
    arr.sort(lambda x: x[0])

    # array to hold the merged intervals
    m = []
    s = -10000
    max = -10000
    for i in range(len(arr)):
        a = arr[i]
        if a[0] > max:
            if i != 0:
                m.append([s, max])
            max = a[1]
            s = a[0]
        else:
            if a[1] >= max:
                max = a[1]
    
