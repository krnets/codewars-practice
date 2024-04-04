import codewars_test as test
from kata import sort_animals, Animal


@test.describe('Example tests')
def example_tests():
    animals = [
        Animal("Cat", 4),
        Animal("Snake", 0),
        Animal("Dog", 4),
        Animal("Centipede", 50),
        Animal("Human", 2),
        Animal("Bird", 2),
        Animal("Cow", 4),
        Animal("Ant", 6)
    ]
    
    sorted_animals = sort_animals(animals) ## Should be: Snake, Bird, Human, Cat, Cow, Dog, Ant, Centipede
    
    @test.it('Regular Case')
    def regular_tests():
        test.assert_equals(sorted_animals[0].name,"Snake")
        test.assert_equals(sorted_animals[0].number_of_legs,0)

        test.assert_equals(sorted_animals[1].name,"Bird")
        test.assert_equals(sorted_animals[1].number_of_legs,2)

        test.assert_equals(sorted_animals[2].name,"Human")
        test.assert_equals(sorted_animals[2].number_of_legs,2)

        test.assert_equals(sorted_animals[3].name,"Cat")
        test.assert_equals(sorted_animals[3].number_of_legs,4)

        test.assert_equals(sorted_animals[4].name,"Cow")
        test.assert_equals(sorted_animals[4].number_of_legs,4)

        test.assert_equals(sorted_animals[5].name,"Dog")
        test.assert_equals(sorted_animals[5].number_of_legs,4)

        test.assert_equals(sorted_animals[6].name,"Ant")
        test.assert_equals(sorted_animals[6].number_of_legs,6)

        test.assert_equals(sorted_animals[7].name,"Centipede")
        test.assert_equals(sorted_animals[7].number_of_legs,50)
