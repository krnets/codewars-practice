import codewars_test as test
from kata import parse_html_color

def should_parse(color, expected):
    actual = parse_html_color(color)
    @test.it('color="{0}"'.format(color))
    def basic_test_cases():
        test.assert_equals(actual, expected)
        
@test.describe("Fixed Tests")
def fixed_tests():
    should_parse('#80FFA0',   {'r': 128, 'g': 255, 'b': 160})
    should_parse('#3B7',      {'r': 51,  'g': 187, 'b': 119})
    should_parse('LimeGreen', {'r': 50,  'g': 205, 'b': 50 })
    should_parse('blue', {'r': 0,  'g': 0, 'b': 255 })
    should_parse('Blue', {'r': 0,  'g': 0, 'b': 255 })
    should_parse('BluE', {'r': 0,  'g': 0, 'b': 255 })
    should_parse('BLUE', {'r': 0,  'g': 0, 'b': 255 })
    should_parse('RED', {'r': 255,  'g': 0, 'b': 0})
    should_parse('GREEN', {'r': 0,  'g': 255, 'b': 0})