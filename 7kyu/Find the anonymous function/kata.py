# def find_function(func, arr):
#     pos = next((i for i, x in enumerate(func) if not isinstance(x, (int, float, str))))
#     return [*filter(func[pos], arr)]


# def find_function(func, arr):
#     pos = next(i for i, x in enumerate(func) if callable(x))
#     return [*filter(func[pos], arr)]


def find_function(func, arr):
    for x in func:
        if callable(x):
            return [*filter(x, arr)]
