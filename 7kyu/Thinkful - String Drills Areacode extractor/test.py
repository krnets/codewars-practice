from kata import area_code
import codewars_test as test

@test.describe("Areacode extractor")
def areacode_extractor():
    
    @test.it("Examples")
    def examples():
        test.assert_equals(area_code("The supplier's phone number is (555) 867-5309"), '555')
        test.assert_equals(area_code("Grae's cell number used to be (123) 456-7890"), '123')
        test.assert_equals(area_code("The 102nd district court's fax line is (124) 816-3264"), '124')