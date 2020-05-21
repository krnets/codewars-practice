# 7kyu - Swap the head and the tail

""" You need to swap the head and the tail of the specified array:

the head (the first half) of array moves to the end, the tail (the second half) moves to the start. 
The middle element (if it exists) leaves on the same position.

Return new array.

    [ 1, 2, 3, 4, 5 ]   =>  [ 4, 5, 3, 1, 2 ]
     \----/   \----/         
      head     tail 

    [ -1, 2 ]  => [ 2, -1 ] 
    [ 1, 2, -3, 4, 5, 6, -7, 8 ]   =>  [ 5, 6, -7, 8, 1, 2, -3, 4 ]   """

# def swap_head_tail(arr):
#     n = len(arr)
#     start = arr[0: n // 2]
#     mid = arr[n // 2: (n + 1) // 2]
#     end = arr[(n + 1) // 2:]
#     return end + mid + start


def swap_head_tail(arr):
    i = len(arr) // 2
    return arr[-i:] + arr[i:-i] + arr[:i]


q = swap_head_tail([1, 2, 3, 4, 5])
q
#      [ 4, 5, 3, 1, 2 ]
q = swap_head_tail([-1, 2])  # [ 2, -1 ]
q
q = swap_head_tail([1, 2, -3, 4, 5, 6, -7, 8])
q
#     [ 5, 6, -7, 8, 1, 2, -3, 4 ])
q = swap_head_tail([-16, -79, 22, -73, 2, 92, 91])
q
q = swap_head_tail([34, -88, -82])
q
