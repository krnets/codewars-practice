#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"
#include <string>

void testequal(std::string ans, std::string sol)
{
	CHECK(ans == sol);
}

void dotest(std::string a1, std::string a2, std::string expected)
{
	testequal(TwoToOne::longest(a1, a2), expected);
}

TEST_CASE("testing longest")
{
	SUBCASE("Fixed__Tests")
	{
		dotest("xyaabbbccccdefww", "xxxxyyyyabklmopq", "abcdefklmopqwxy");
		dotest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz");
		dotest("aretheyhere", "yestheyarehere", "aehrsty");
		dotest("loopingisfunbutdangerous", "lessdangerousthancoding", "abcdefghilnoprstu");
		dotest("inmanylanguages", "theresapairoffunctions", "acefghilmnoprstuy");
		dotest("lordsofthefallen", "gamekult", "adefghklmnorstu");
		dotest("codewars", "codewars", "acdeorsw");
		dotest("agenerationmustconfrontthelooming", "codewarrs", "acdefghilmnorstuw");
	}
}
