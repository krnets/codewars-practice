import codewars_test as test
from kata import last_index_of, lst_to_link

@test.describe('Example Tests')
def example_tests():
    @test.it('Integers example Test Cases')
    def integers_example_test_cases():
        head = None
        test.assert_equals(last_index_of(head, 17), -1)
        
        head = lst_to_link([1, 2, 3])
        test.assert_equals(last_index_of(head, 2), 1)

        head = lst_to_link([1, 2, 3, 3])
        test.assert_equals(last_index_of(head, 3), 3)
    
    @test.it('strings example Test Cases')
    def strings_example_test_cases():
        head = lst_to_link(["aaa", "b", "abc"])
        test.assert_equals(last_index_of(head, "aaa"), 0)
        
        head = lst_to_link(["aaa", "b", "abc"])
        test.assert_equals(last_index_of(head, "c"), -1)
    
    @test.it('Mixed types example Test Cases')
    def mixed_types_example_test_cases():
        head = lst_to_link([17, "17", 1.2])
        test.assert_equals(last_index_of(head, 17), 0)
        
        head = lst_to_link([17, "17", 1.2])
        test.assert_equals(last_index_of(head, "17"), 1)
