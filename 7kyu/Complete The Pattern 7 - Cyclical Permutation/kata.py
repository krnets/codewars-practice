def pattern(n):
    return "\n".join("".join(str((i + j) % n + 1) for j in range(n)) for i in range(n))