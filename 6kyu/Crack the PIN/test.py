import codewars_test as test
from kata import crack

@test.describe("Should pass all of these")

def exampleTests():
    @test.it("Sample test 1")
    def sampleTest1():
        test.assert_equals(crack("827ccb0eea8a706c4c34a16891f84e7b"), "12345")
        
    @test.it("Sample test 2")
    def sampleTest2():
        test.assert_equals(crack("86aa400b65433b608a9db30070ec60cd"), "00078")