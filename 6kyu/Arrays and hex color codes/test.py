import codewars_test as test
from kata import get_colors

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        col_arr = [ [ "6B8E23", "9ACD32","2E8B57","00008B", "00FF00","6B8E23","00FA9A" ],
        [ "CD5C5C", "8B0000", "FF0000", "F08080", "98FB98", "DC143C" ],
        [ "00BFFF", "00008B", "B22222", "000080", "87CEEB", "4169E1" ] ]
        test.assert_equals(get_colors(col_arr),"Green+Blue,Red+Green,Blue+Red")

        col_arr = [[ "FF0000", "191970", "FF0000" ],
        [ "556B2F", "98FB98", "2E8B57", "00FF7F", "556B2F", "FFA07A" ],
        [ "00BFFF", "00BFFF", "4169E1", "1E90FF", "F08080", "191970" ] ]
        test.assert_equals(get_colors(col_arr),"Red+Blue,Green+Red,Blue+Red")

        col_arr = [ [ "FF0000", "8DC4DE", "87CEFA", "4169E1", "0000FF" ],
        [ "FF0000", "191970", "00008B" ],
        [ "CD5C5C", "F08080", "0000FF" ] ]
        test.assert_equals(get_colors(col_arr),"Blue+Red,Blue+Red,Red+Blue")