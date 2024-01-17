# def scale(strng, k, v):
#     res = []

#     for line in strng.splitlines():
#         sub = ""
#         for c in line:
#             sub += c * k
#         for _ in range(v):
#             res.append(sub)

#     return "\n".join(res)


def scale(strng, k, v):
    return "\n".join(
        "\n".join(["".join(c * k for c in line)] * v) for line in strng.splitlines()
    )


# Example: a = "abcd\nefgh\nijkl\nmnop"
# scale(a, 2, 3)

# abcd   ----->   aabbccdd
# efgh            aabbccdd
# ijkl            aabbccdd
# mnop            eeffgghh
#                 eeffgghh
#                 eeffgghh
#                 iijjkkll
#                 iijjkkll
#                 iijjkkll
#                 mmnnoopp
#                 mmnnoopp
#                 mmnnoopp
