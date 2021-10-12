#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing get_order")
{
	SUBCASE("sample test 1")
	{
		CHECK(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza") ==
			"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke");
	}
	SUBCASE("sample test 2")
	{
		CHECK(get_order("pizzachickenfriesburgercokemilkshakefriessandwich") ==
			"Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke");
	}
}
