# def draw_stairs(n):
#     stairs = ['I'] * n
#     return '\n'.join(' ' * i + x for i, x in enumerate(stairs))

# def draw_stairs(n):
#     return '\n'.join(' ' * i + 'I' for i in range(n))

def draw_stairs(n):
    return '\n'.join('I'.rjust(i+1) for i in range(n))
