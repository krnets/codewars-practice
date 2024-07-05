import codewars_test as test
import ipaddress
import socket


# def is_valid_IP(strng):
#     try:
#         ipaddress.ip_address(strng)
#         return True
#     except:
#         return False


# def is_valid_IP(strng):
#     try:
#         socket.inet_pton(socket.AF_INET, strng)
#         return True
#     except:
#         return False


# def is_valid_IP(strng):
#     return (
#         (octets := strng.split("."))
#         and len(octets) == 4
#         and all(
#             octet.isnumeric()
#             and 0 <= int(octet) <= 255
#             and not (octet[0] == "0" and len(octet) > 1)
#             for octet in octets
#         )
#     )


def is_valid_IP(strng):
    return (
        (octets := strng.split("."))
        and len(octets) == 4
        and all(
            octet.isnumeric() 
            and 0 <= (x := int(octet)) <= 255 
            and octet == str(x)
            for octet in octets
        )
    )


@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(is_valid_IP("12.255.56.1"), True)
        test.assert_equals(is_valid_IP(""), False)
        test.assert_equals(is_valid_IP("abc.def.ghi.jkl"), False)
        test.assert_equals(is_valid_IP("123.456.789.0"), False)
        test.assert_equals(is_valid_IP("12.34.56"), False)
        test.assert_equals(is_valid_IP("12.34.56 .1"), False)
        test.assert_equals(is_valid_IP("12.34.56.-1"), False)
        test.assert_equals(is_valid_IP("123.045.067.089"), False)
        test.assert_equals(is_valid_IP("127.1.1.0"), True)
        test.assert_equals(is_valid_IP("0.0.0.0"), True)
        test.assert_equals(is_valid_IP("0.34.82.53"), True)
        test.assert_equals(is_valid_IP("192.168.1.300"), False)
