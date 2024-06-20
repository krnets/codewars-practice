import codewars_test as test
from kata import find_odd_names

@test.describe('Fixed Tests')
def example_tests():

    @test.it('Example Test Case')
    def example_test_case():
        
        list1 = [
          { 'firstName': 'Aba', 'lastName': 'N.', 'country': 'Ghana', 'continent': 'Africa', 'age': 21, 'language': 'Python' },
          { 'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java' }
        ]
        
        answer1 = [
          { 'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java' }
        ];
        
        test.assert_equals(find_odd_names(list1), answer1)
        
        
        list2 = [
          { 'firstName': 'Aba', 'lastName': 'N.', 'country': 'Ghana', 'continent': 'Africa', 'age': 21, 'language': 'Python' },
        ];
        
        answer2 = []
        
        test.assert_equals(find_odd_names(list2), answer2)
        