""" 7kyu - Triangular range

Triangular numbers count the number of objects that can form an equilateral triangle. 
The nth triangular number forms an equilateral triangle with n dots on each side (including the vertices). 
Here is a graphic example for the triangular numbers of 1 to 5:

n=1: triangular number: 1
*

n=2: triangular number: 3
 *
* *

n=3: triangular number: 6
  *
 * *
* * *

n=4: triangular number: 10
    *
   * *
  * * *
 * * * *

 n=5: triangular number: 15
      *
     * *
    * * *
   * * * *
  * * * * *

Your task is to implement a function triangular_range(start, stop) that returns a dictionary of all numbers 
as keys and the belonging triangular numbers as values, where the triangular number is in the range start, stop 
(including start and stop). 

For example, triangular_range(1, 3) should return {1: 1, 2: 3} 
and triangular_range(5, 16) should return {3: 6, 4: 10, 5: 15}. """


# def triangular_range(start, stop):
#     res = dict()
#     for i in range(1, stop):
#         triangular = i * (i+1) // 2
#         if start <= triangular <= stop:
#             res.setdefault(i, triangular)
#     return res

def triangular_range(start, stop):
    tri = n = 1
    res = {}
    while tri <= stop:
        if tri >= start:
            res[n] = tri
        n += 1
        tri = n * (n+1) // 2
    return res


q = triangular_range(1, 3), {1: 1, 2: 3}
q
q = triangular_range(5, 16), {3: 6, 4: 10, 5: 15}
q
