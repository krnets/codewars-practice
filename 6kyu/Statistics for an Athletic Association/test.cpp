#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

static void dotest(const string& lst, string& expected)
{
	CHECK(Stat::stat(lst) == expected);
}

TEST_CASE("testing stat_Tests")
{
	SUBCASE("Fixed_Tests 1")
	{
		string l = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17";
		string sol = "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34";
		dotest(l, sol);
	}
	SUBCASE("Fixed_Tests 2")
	{
		string l = "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41";
		string sol = "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00";
		dotest(l, sol);
	}
}
