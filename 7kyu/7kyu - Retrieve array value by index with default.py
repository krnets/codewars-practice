# 7kyu - Retrieve array value by index with default

""" Retrieve the value of the array at the index provided. 
If the index is out of the array's max bounds then it should return the default value instead.

data = ['a', 'b', 'c']
solution(data, 1, 'd') # should == 'b'
solution(data, 5, 'd') # should == 'd'

# negative values work as long as they aren't out of the length bounds
solution(data, -1, 'd') # should == 'c'
solution(data, -5, 'd') # should == 'd' """


# def solution(items, index, default_value):
#     return items[index] if abs(index+1) < len(items) else default_value

def solution(items, index, default_value):
    try:
        return items[index]
    except IndexError:
        return default_value


arr = list(range(1, 4))
q = solution(arr, 1, 'a')  # 2
q
q = solution(arr, -1, 'a')  # 3
q
q = solution(arr, -5, 'a')  # 'a'
q
q = solution(arr, -3, 'a')  # 1
q

arr = list(range(1, 6))
q = solution(range(1, 6), 10, 'a')  # 'a'
q
q = solution([None, None], 0, 'a')  # None
q
