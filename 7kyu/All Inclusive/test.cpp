#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(bool ans, bool sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing containAllRots_Tests")
{
	SUBCASE("Fixed_Tests")
	{
		std::string s1 = "bsjq";
		std::vector<std::string> v1 = {"bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"};
		bool b = Rotations::containAllRots(s1, v1);
		testequal(b, true);
		s1 = "";
		v1 = {};
		b = Rotations::containAllRots(s1, v1);
		testequal(b, true);
		s1 = "";
		v1 = {"bsjq", "qbsj"};
		b = Rotations::containAllRots(s1, v1);
		testequal(b, true);
		s1 = "XjYABhR";
		v1 = {"TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"};
		b = Rotations::containAllRots(s1, v1);
		testequal(b, false);
	}
}
