#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sample_test")
{
	using VI = vector<string>;

	SUBCASE("even_length")
	{
		CHECK(solution("abcdef") == VI{"ab", "cd", "ef"});
		CHECK(solution("HelloWorld") == VI{"He", "ll", "oW", "or", "ld"});
	}
	SUBCASE("odd_length")
	{
		CHECK(solution("abcde") == VI{"ab", "cd", "e_"});
		CHECK(solution("LovePizza") == VI{"Lo", "ve", "Pi", "zz", "a_"});
	}
}
