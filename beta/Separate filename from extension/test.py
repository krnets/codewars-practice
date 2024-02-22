import codewars_test as test
from kata import separate_filename_from_extension


test.describe("Given an absolute path should correctly separate filename from extension")
test.it("Can handle regular path")
file_path = "/some/path/to/file.txt"
expected = ("/some/path/to/file", ".txt")
test.assert_equals(separate_filename_from_extension(file_path), expected)

file_path = "/some/path/to/file.tar.gz"
expected = ("/some/path/to/file", ".tar.gz")
test.assert_equals(separate_filename_from_extension(file_path), expected)

file_path = "/another/path/to/data.csv.gz"
expected = ("/another/path/to/data", ".csv.gz")
test.assert_equals(separate_filename_from_extension(file_path), expected)

test.it("Can handle hidden directory in path")
file_path = "/some/path/.to/file.txt"
expected = ("/some/path/.to/file", ".txt")
test.assert_equals(separate_filename_from_extension(file_path), expected)

test.it("Can handle empty string")
expected = ("", "")
test.assert_equals(separate_filename_from_extension(""), expected)

test.it("Can handle long extension")
file_path = "/some/path/.to/file.txt.gz"
expected = ("/some/path/.to/file", ".txt.gz")
test.assert_equals(separate_filename_from_extension(file_path), expected)

test.it("Can handle hidden file")
file_path = "/some/path/.file.tar.gz"
expected = ("/some/path/.file", ".tar.gz")
test.assert_equals(separate_filename_from_extension(file_path), expected)

test.it("Can handle file without extension")
file_path = "/some/path/file"
expected = ("/some/path/file", "")
test.assert_equals(separate_filename_from_extension(file_path), expected)

test.it("Can handle hidden file without extension")
file_path = "/some/path/.file"
expected = ("/some/path/.file", "")
test.assert_equals(separate_filename_from_extension(file_path), expected)
