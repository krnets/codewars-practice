#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple_string_characters")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve("Codewars@codewars123.com") == std::vector<int>{1, 18, 3, 2});
		CHECK(solve("bgA5<1d-tOwUZTS8yQ") == std::vector<int>{7, 6, 3, 2});
		CHECK(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H") == std::vector<int>{9, 9, 6, 9});
		CHECK(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD") == std::vector<int>{15, 8, 6, 9});
	}
}
