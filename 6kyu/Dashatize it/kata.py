def dashatize(n):
    return (
        "".join(f"-{i}-" if i & 1 else str(i) for i in map(int, str(abs(n))))
        .replace("--", "-")
        .strip("-")
    )
