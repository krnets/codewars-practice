from timeit import timeit

def performance_test(fct, arguments, repetitions=10000):
    duration = timeit(
        lambda x=arguments: fct(*arguments), number=repetitions)
    print("{0} took {1} secs to complete {2} repetitions".format(
        fct.__name__, duration, repetitions))

arr1, arr2 = list(range(100000)), list(range(100000,200000))

def array_plus_array1(arr1,arr2):
    return sum(arr1 + arr2)

def array_plus_array2(arr1,arr2):
    return sum(arr1) + sum(arr2)

def array_plus_array3(*args):
    return sum(map(sum, args))

performance_test(array_plus_array1, [arr1, arr2], 100)
performance_test(array_plus_array2, [arr1, arr2], 100)
performance_test(array_plus_array3, [arr1, arr2], 100)