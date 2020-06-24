""" 7kyu - Bubble Sort

Since everybody hates chaos and loves sorted lists we should implement some more sorting algorithms. 
Your task is to implement a Bubble sort (for some help look at https://en.wikipedia.org/wiki/Bubble_sort) 
and return a list of snapshots after each change of the initial list.

If the initial list would be l=[1,2,4,3] my algorithm rotates l[2] and l[3] and after that it adds [1,2,3,4] 
to the result, which is a list of snapshots.

[1,2,4,3] should return [ [1,2,3,4] ]
[2,1,4,3] should return [ [1,2,4,3], [1,2,3,4] ]
[1,2,3,4] should return [] """


def bubble(l):
    snapshots = []
    for i in range(len(l)-1):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                snapshots.append(l[:])
    return snapshots


l = [1, 2, 4, 3]
sol = [[1, 2, 3, 4]]
q = bubble(l), sol
q

l = [2, 1, 4, 3]
sol = [[1, 2, 4, 3], [1, 2, 3, 4]]
q = bubble(l), sol
q

l = [1, 4, 3, 6, 7, 9, 2, 5, 8]
sol = [[1, 3, 4, 6, 7, 9, 2, 5, 8],
       [1, 3, 4, 6, 7, 2, 9, 5, 8],
       [1, 3, 4, 6, 7, 2, 5, 9, 8],
       [1, 3, 4, 6, 7, 2, 5, 8, 9],
       [1, 3, 4, 6, 2, 7, 5, 8, 9],
       [1, 3, 4, 6, 2, 5, 7, 8, 9],
       [1, 3, 4, 2, 6, 5, 7, 8, 9],
       [1, 3, 4, 2, 5, 6, 7, 8, 9],
       [1, 3, 2, 4, 5, 6, 7, 8, 9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9]]
q = bubble(l), sol
q
