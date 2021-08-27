#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include <fmt/core.h>
#include "solve.h"

inline std::string pair2str(const std::pair<std::string, std::string>& p)
{
	return fmt::format(R"(\{}\{}\)", p.first, p.second);
}

void doTest(const std::string& s, const std::pair<std::string, std::string>& expected)
{
	const auto actual = capitalize(s);
	CHECK(pair2str(actual) == pair2str(expected));
}

TEST_CASE("testing capitalize")
{
	SUBCASE("Basic_tests")
	{
		doTest("abcdef", {"AbCdEf", "aBcDeF"});
		doTest("codewars", {"CoDeWaRs", "cOdEwArS"});
		doTest("abracadabra", {"AbRaCaDaBrA", "aBrAcAdAbRa"});
		doTest("codewarriors", {"CoDeWaRrIoRs", "cOdEwArRiOrS"});
	}
}
