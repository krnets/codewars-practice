#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing Expressions_Matter")
{
	SUBCASE("Check_Small_Values")
	{
		CHECK(expressionsMatter(2, 1, 2) == 6);
		CHECK(expressionsMatter(2, 1, 1) == 4);
		CHECK(expressionsMatter(1, 1, 1) == 3);
		CHECK(expressionsMatter(1, 2, 3) == 9);
		CHECK(expressionsMatter(1, 3, 1) == 5);
		CHECK(expressionsMatter(2, 2, 2) == 8);
	}
	SUBCASE("Check_Intermediate_Values")
	{
		CHECK(expressionsMatter(5, 1, 3) == 20);
		CHECK(expressionsMatter(3, 5, 7) == 105);
		CHECK(expressionsMatter(5, 6, 1) == 35);
		CHECK(expressionsMatter(1, 6, 1) == 8);
		CHECK(expressionsMatter(2, 6, 1) == 14);
		CHECK(expressionsMatter(6, 7, 1) == 48);
	}
	SUBCASE("Check_Mixed_Values")
	{
		CHECK(expressionsMatter(2, 10, 3) == 60);
		CHECK(expressionsMatter(1, 8, 3) == 27);
		CHECK(expressionsMatter(9, 7, 2) == 126);
		CHECK(expressionsMatter(1, 1, 10) == 20);
		CHECK(expressionsMatter(9, 1, 1) == 18);
		CHECK(expressionsMatter(10, 5, 6) == 300);
		CHECK(expressionsMatter(1, 10, 1) == 12);
	}
}
