import codewars_test as test
from kata import find_senior

@test.describe('Example Tests')
def example_tests():
    @test.it('Example Test Case')
    def example_test_case():    
        list1 = [
            { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
            { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
            { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
            { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
            ]        
        answer1 = [
            { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
            { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
            ]
        test.assert_equals(find_senior(list1), answer1)        
        
        list2 = [
            { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
            { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
            { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
            ]        
        answer2 = [
            { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
            ]
        test.assert_equals(find_senior(list2), answer2)        
        
        list3 = [
            { 'firstName': 'Alexander', 'lastName': 'F.', 'country': 'Russia', 'continent': 'Europe', 'age': 89, 'language': 'Java' },
            { 'firstName': 'Fatima', 'lastName': 'K.', 'country': 'Saudi Arabia', 'continent': 'Asia', 'age': 21, 'language': 'Clojure' },
            { 'firstName': 'Mark', 'lastName': 'G.', 'country': 'Scotland', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
            { 'firstName': 'Nikola', 'lastName': 'H.', 'country': 'Serbia', 'continent': 'Europe', 'age': 29, 'language': 'Python' },
            { 'firstName': 'Jakub', 'lastName': 'I.', 'country': 'Slovakia', 'continent': 'Europe', 'age': 28, 'language': 'Java' },
            { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 89, 'language': 'JavaScript' },
            { 'firstName': 'Luka', 'lastName': 'J.', 'country': 'Slovenia', 'continent': 'Europe', 'age': 29, 'language': 'Clojure' },
            { 'firstName': 'Mariam', 'lastName': 'B.', 'country': 'Egypt', 'continent': 'Africa', 'age': 89, 'language': 'Python' },
            ]
        
        answer3 = [
            { 'firstName': 'Alexander', 'lastName': 'F.', 'country': 'Russia', 'continent': 'Europe', 'age': 89, 'language': 'Java' },
            { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 89, 'language': 'JavaScript' },
            { 'firstName': 'Mariam', 'lastName': 'B.', 'country': 'Egypt', 'continent': 'Africa', 'age': 89, 'language': 'Python' },
            ]
        test.assert_equals(find_senior(list3), answer3);