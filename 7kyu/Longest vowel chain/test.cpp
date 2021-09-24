#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple_Square_numbers")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve("ultrarevolutionariees") == 3);
		CHECK(solve("codewarriors") == 2);
		CHECK(solve("suoidea") == 3);
		CHECK(solve("strengthlessnesses") == 1);
		CHECK(solve("mnopqriouaeiopqrstuvwxyuaeiouaeiou") == 11);
	}
}
