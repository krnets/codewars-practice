#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing findNextSquareTests")
{
	SUBCASE("BasicTests")
	{
		CHECK(findNextSquare(121) == 144);
		CHECK(findNextSquare(625) == 676);
		CHECK(findNextSquare(319225) == 320356);
		CHECK(findNextSquare(15241383936) == 15241630849);
		CHECK(findNextSquare(155) == -1);
		CHECK(findNextSquare(114) == -1);
	}
}
