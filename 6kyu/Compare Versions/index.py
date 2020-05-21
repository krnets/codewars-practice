# 6kyu - Compare Versions

""" Karan's company makes software that provides different features based on the version of operating system of the user.

For finding which version is more recent, Karan uses the following method:

While this function worked for OS versions 10.6, 10.7, 10.8 and 10.9, the Operating system company just released OS version 10.10.

Karan's function fails for the new version:

compare_versions ("10.9", "10.10");       # returns True, while it should return False

Karan now wants to spend some time to right a more robust version comparison function that works 
for any future version/sub-version updates.

Help Karan write this function. Here are a few sample cases:

compare_versions("11", "10");                    # returns True
compare_versions("11", "11");                    # returns True
compare_versions("10.4.6", "10.4");              # returns True
compare_versions("10.4", "11");                  # returns False
compare_versions("10.4", "10.10");               # returns False
compare_versions("10.4.9", "10.5");              # returns False

It can be assumed that version strings are non empty and only contain numeric literals and the character '.'. """

# def compare_versions(version1, version2):
#     v1 = [int(x) for x in version1.split('.')]
#     v2 = [int(x) for x in version2.split('.')]
#     if len(v1) == 1: v1.append(0)
#     if len(v1) == 2: v1.append(0)
#     if len(v2) == 1: v2.append(0)
#     if len(v2) == 2: v2.append(0)
#     return v1 >= v2

# def compare_versions(v1, v2):
#     return [int(x) for x in v1.split('.')] >= [int(x) for x in v2.split('.')]

from distutils.version import LooseVersion

def compare_versions(version1, version2):
    return LooseVersion(version1) >= LooseVersion(version2)


q = compare_versions("11", "10")  # True, 'Testing versions without subversion'
q
q = compare_versions("11", "11")  # True
q
q = compare_versions("10.4.6", "10.4")
q
#      True, 'Adding a subversion should make this version "larger"'
q = compare_versions("10.4", "10.4.8")
q
#      False, 'Adding a subversion should make this version "larger"'
q = compare_versions("10.4", "11")
q
#      False, 'Subversion precedence is smaller than Version'
q = compare_versions("10.4", "10.10")
q
#      False, 'Version value is not the same as its decimal value'
q = compare_versions("10.4.9", "10.5")
q
#      False, 'Adding subversion does not make it larger than a greater version'
