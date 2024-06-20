import codewars_test as test
from kata import is_language_diverse

@test.describe('Sample Test Cases')
def example_tests():

    @test.it('Example Test Case')
    def example_test_case():
        list1 = [
          { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
          { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 43, 'language': 'Ruby' },
          { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 95, 'language': 'JavaScript' },
          { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
          { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
        ]
        
        list2 = [
          { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
          { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 95, 'language': 'JavaScript' },
          { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
          { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
        ]
        
        list3 = [
          { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
          { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
          { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
        ]
        
        list4 = [
          { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
          { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
        ]

        test.assert_equals(is_language_diverse(list1), False)
        test.assert_equals(is_language_diverse(list2), False)
        test.assert_equals(is_language_diverse(list3), True)
        test.assert_equals(is_language_diverse(list4), True)

