#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"


void testequal(string ans, string sol)
{
	CHECK(ans == sol);
}

template <typename Func>
static void dotest(Func func, string s, string expected)
{
	testequal(Opstrings1::oper(func, s), expected);
}

TEST_CASE("testing oper_Tests")
{
	SUBCASE("rot_Tests")
	{
		string s = "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL";
		string sol = "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif";
		dotest(Opstrings1::rot, s, sol);
		s = "rkKv\ncofM\nzXkh\nflCB";
		sol = "BClf\nhkXz\nMfoc\nvKkr";
		dotest(Opstrings1::rot, s, sol);
	}
	SUBCASE("selfieAndRot_Tests")
	{
		string s = "xZBV\njsbS\nJcpN\nfVnP";
		string sol = "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx";
		dotest(Opstrings1::selfieAndRot, s, sol);

		s = "xZBV\njsbS\nJcpN\nfVnP";
		sol = "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx";
		dotest(Opstrings1::selfieAndRot, s, sol);
	}
}
