""" 7kyu - Quicksum

A checksum is an algorithm that scans a packet of data and returns a single number. 
The idea is that if the packet is changed, the checksum will also change, 
so checksums are often used for detecting transmission errors, validating document contents, 
and in many other situations where it is necessary to detect undesirable changes in data.

For this problem, you will implement a checksum algorithm called Quicksum. 
A Quicksum packet allows only uppercase letters and spaces. 
It always begins and ends with an uppercase letter.

Otherwise, spaces and uppercase letters can occur in any combination, including consecutive spaces.

A Quicksum is the sum of the products of each character’s position in the packet times the character’s value. 
A space has a value of zero, while letters have a value equal to their position in the alphabet.

So, A = 1, B = 2, etc., through Z = 26. Here are example Quicksum calculations for the packets “ACM” and “A C M”:
  
ACM
1 × 1 + 2 × 3 + 3 × 13 = 46 

A C M
1 x 1 + 3 x 3 + 5 * 13 = 75

When the packet doesn't have only uppercase letters and spaces or just spaces the result to quicksum have to be zero (0).

"""

from string import ascii_uppercase as ABC
import re

# def quicksum(packet):
#     if bool(re.findall(r'[^A-Z\s]', packet)):
#         return 0
    #  return sum((i+1) * (ABC.index(x)+1) if x in ABC else 0 for i, x in enumerate(packet))


def quicksum(packet):
    return sum(i * (ABC.index(x)+1) if x.isupper() else 0 for i, x in enumerate(packet, 1)) if re.match(r'[A-Z\s]*$', packet) else 0


q = quicksum("ACM"), 46
q
q = quicksum("MID CENTRAL"), 650
q
q = quicksum("BBC"), 15
q
q = quicksum("234 234 WEF ASDF AAA 554211 ???? "), 0
q
q = quicksum("AbqTH #5"), 0
q
