#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing CreatePhoneNumber")
{
	SUBCASE("BasicTests")
	{
		using arr = int [10];

		CHECK(createPhoneNumber(arr{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) == "(123) 456-7890");
		CHECK(createPhoneNumber(arr{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}) == "(111) 111-1111");
		CHECK(createPhoneNumber(arr{1, 2, 3, 4, 5, 6, 8, 8, 0, 0}) == "(123) 456-8800");
		CHECK(createPhoneNumber(arr{0, 2, 3, 0, 5, 6, 0, 8, 9, 0}) == "(023) 056-0890");
		CHECK(createPhoneNumber(arr{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}) == "(000) 000-0000");
	}
}
