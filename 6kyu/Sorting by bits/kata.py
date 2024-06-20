# def sort_by_bit(arr):
#     arr.sort(key=lambda x: (x.bit_count(), x))
#     return arr

# def sort_by_bit(arr):
#     arr.sort() or arr.sort(key=int.bit_count)

from gmpy2 import popcount

def sort_by_bit(arr):
    arr.sort() or arr.sort(key=popcount)