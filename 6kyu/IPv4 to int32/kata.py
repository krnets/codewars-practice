# def ip_to_int32(ip):
#     ans = 0
#     for i, octet in enumerate(reversed(ip.split("."))):
#         x = int(octet) << (i*8)
#         ans = ans | x
#     return ans

# from ipaddress import IPv4Address

# def ip_to_int32(ip):
#     return int(IPv4Address(ip))


# def ip_to_int32(ip):
#     return int("".join(f"{octet:08b}" for octet in map(int, ip.split("."))), 2)


def ip_to_int32(ip):
    ans = 0
    for i, octet in enumerate(map(int, reversed(ip.split(".")))):
        ans |= octet << (i * 8)
    return ans
