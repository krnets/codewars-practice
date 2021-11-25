#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple Simple Simple String Expansion")
{
	SUBCASE("Sample_Tests")
	{
		CHECK(string_expansion("3abc") == "aaabbbccc");
		CHECK(string_expansion("3D2a5d2f") == "DDDaadddddff");
		CHECK(string_expansion("0d0a0v0t0y") == "");
		CHECK(string_expansion("3d332f2a") == "dddffaa");
		CHECK(string_expansion("abcde") == "abcde");
	}
}
