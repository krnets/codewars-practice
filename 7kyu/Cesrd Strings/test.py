import codewars_test as test
from kata import uncensor


@test.describe("Ce*s*r*d Strings")
def examples():
    @test.it("Example Tests")
    def example_fixed():
        data = [
            ("*h*s *s v*ry *tr*ng*", "Tiiesae", "This is very strange"),
            ("A**Z*N*", "MAIG", "AMAZING"),
            ("xyz", "", "xyz"),
            ("", "", ""),
            ("***", "abc", "abc"),
        ]

        for infected, discovered, result in data:
            test.assert_equals(uncensor(infected, discovered), result)
