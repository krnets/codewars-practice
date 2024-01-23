# def histogram(results):
#     lines = [
#         f'{i}|{"#" * v}' + (f" {v}" if v else "") + "\n"
#         for i, v in enumerate(results, 1)
#     ]
#     return "".join(reversed(lines))


def histogram(results):
    return "".join(
        reversed(
            [f'{i}|{"#" * v}' + (f" {v}" if v else "") + "\n"
                for i, v in enumerate(results, 1)])
        )