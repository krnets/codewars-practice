#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ExampleTests")
{
	SUBCASE("BasicTest")
	{
		std::string expected =
			"6|##### 5\n"
			"5|\n"
			"4|# 1\n"
			"3|########## 10\n"
			"2|### 3\n"
			"1|####### 7\n";

		std::string actual = histogram({7, 3, 10, 1, 0, 5});

		CHECK(actual == expected);
	}
}
