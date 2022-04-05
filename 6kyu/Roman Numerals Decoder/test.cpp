#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing your_roman_numerals_decoder_solution")
{
	SUBCASE("sample tests")
	{
		CHECK(solution("I") == 1);
		CHECK(solution("IV") == 4);
		CHECK(solution("XXI") == 21);
		CHECK(solution("MMVIII") == 2008);
		CHECK(solution("MDCLXVI") == 1666);
	}
}
