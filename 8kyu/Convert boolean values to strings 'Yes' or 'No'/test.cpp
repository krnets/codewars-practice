#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing bool_to_word_method")
{
	SUBCASE("basic_tests")
	{
		CHECK(bool_to_word(true) == "Yes");
		CHECK(bool_to_word(false) == "No");
	}
}
