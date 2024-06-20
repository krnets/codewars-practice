# def cookie(x):
#     if isinstance(x, str):
#         return f"Who ate the last cookie? It was Zach!"
#     if isinstance(x, bool):
#         return f"Who ate the last cookie? It was the dog!"
#     if x == 'Ryan':
#         return f"Who ate the last cookie? It was {x}!"
#     if isinstance(x, (int, float)):
#         return f"Who ate the last cookie? It was Monica!"


def cookie(x):
    d = {str: "Zach", bool: "the dog"}
    return f"Who ate the last cookie? It was {d.get(type(x), 'Monica')}!"
