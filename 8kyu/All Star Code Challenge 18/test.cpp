#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing StrCount")
{
	SUBCASE("BasicTests")
	{
		CHECK(strCount("Hello", 'o') == 1);
		CHECK(strCount("Hello", 'l') == 2);
		CHECK(strCount("Hello", 'q') == 0);
		CHECK(strCount("Pippi", 'p') == 2);
		CHECK(strCount("", 'l') == 0);
	}
}
