import codewars_test as test
from kata import get_order

test.assert_equals(
    get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"),
    "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke",
)
test.assert_equals(
    get_order("pizzachickenfriesburgercokemilkshakefriessandwich"),
    "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke",
)
