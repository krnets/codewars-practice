#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	SUBCASE("Sample_cases")
	{
		CHECK(switcheroo("abc") == "bac");
		CHECK(switcheroo("aaabcccbaaa") == "bbbacccabbb");
		CHECK(switcheroo("cccccc") == "cccccc");
		CHECK(switcheroo("abababababababab") == "babababababababa");
		CHECK(switcheroo("aaaa") == "bbbb");
		CHECK(switcheroo("bbbb") == "aaaa");
	}
}
