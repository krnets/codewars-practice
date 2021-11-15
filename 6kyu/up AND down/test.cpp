#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void dotest(std::string s, std::string expected)
{
	CHECK(UpAndDown::arrange(s) == expected);
}

TEST_CASE("testing up AND down")
{
	SUBCASE("Fixed__Tests")
	{
		std::string s = "who hit retaining The That a we taken";
		std::string sol = "who RETAINING hit THAT a THE we TAKEN";
		dotest(s, sol);
		s = "on I came up were so grandmothers";
		sol = "i CAME on WERE up GRANDMOTHERS so";
		dotest(s, sol);
		s = "way the my wall them him";
		sol = "way THE my WALL him THEM";
		dotest(s, sol);
	}
}
