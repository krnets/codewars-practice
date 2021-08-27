#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing mxdiflg")
{
	SUBCASE("Fixed__Tests")
	{
		using V = std::vector<std::string>;

		auto s1 = V{
			"hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"
		};
		auto s2 = V{"cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"};
		CHECK(MaxDiffLength::mxdiflg(s1, s2) == 13);

		s1 = V{"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"};
		s2 = V{"bbbaaayddqbbrrrv"};
		CHECK(MaxDiffLength::mxdiflg(s1, s2) == 10);
	}
}
