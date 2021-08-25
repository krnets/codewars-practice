#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing endswith")
{
	SUBCASE("Sample_Test_Cases")
	{
		CHECK(solution("abcde", "cde") == true);
		CHECK(solution("abcde", "abc") == false);
		CHECK(solution("abc", "") == true);
	}
}
