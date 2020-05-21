""" 8kyu - Swap Values """

def swap_values(args): 
    args[0], args[1] = args[1], args[0]
    return args

arr = [1, 2]
q = swap_values(arr) # [2, 1]
q