""" 7kyu - Simple Fun #138: Similarity

Your task is to find the similarity of given sorted arrays a and b, which is defined as follows:
You take the number of elements which are present in both arrays and divide it by the number 
of elements which are present in at least one array.

It also can be written as a formula similarity(A, B) = #(A ∩ B) / #(A ∪ B), 
where #(C) is the number of elements in C, ∩ is intersection of arrays, ∪ is union of arrays.

This is known as Jaccard similarity.

The result is guaranteed to fit any floating-point type without rounding.

For a = [1, 2, 4, 6, 7] and b = [2, 3, 4, 7]:

elements [2, 4, 7] are present in both arrays;
elements [1, 2, 3, 4, 6, 7] are present in at least one of the arrays.
So the similarity equals to 3 / 6 = 0.5.```

 - `[input]` integer array `a`
  A `sorted` array of positive integers. 
  All elements are `different` and are `less than 100`.
  `1 ≤ a.length ≤ 100`

 - `[input]` integer array `b`
  An array in the same format as `a`.

 - `[output]` a float number
  The similarity of the arrays. """


# def similarity(a, b):
#     return len(set(a).intersection(b)) / len(set(a + b))

def similarity(a, b):
    return len(set(a).intersection(set(b))) / len(set(a + b))


q = similarity([1, 2, 3], [1, 2, 3]), 1
q
q = similarity([1, 2, 3], [4, 5, 6]), 0
q
q = similarity([1, 2, 4, 6, 7], [2, 3, 4, 7]), 0.5
q
q = similarity([1, 2, 6, 8, 9], [0, 1, 4, 5, 6, 8, 9]), 0.5
q
q = similarity([1, 2, 3, 4, 7, 9], [1, 2, 3]), 0.5
q
q = similarity([0, 1, 3, 4, 5, 6, 9, 14, 15, 16, 17, 18, 19], [1, 4, 10, 12, 13, 14, 15, 16]), 0.3125
q
