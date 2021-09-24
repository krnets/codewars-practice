#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing cat_mouse")
{
	SUBCASE("Should_escape")
	{
		CHECK(cat_mouse("C....m") == "Escaped!");
		CHECK(cat_mouse("C.....m") == "Escaped!");
		CHECK(cat_mouse("C.......m") == "Escaped!");
		CHECK(cat_mouse("m.....C") == "Escaped!");
	}
	SUBCASE("Should_be_caught")
	{
		CHECK(cat_mouse("C...m") == "Caught!");
		CHECK(cat_mouse("C..m") == "Caught!");
		CHECK(cat_mouse("C.m") == "Caught!");
		CHECK(cat_mouse("m...C") == "Caught!");
	}
}
