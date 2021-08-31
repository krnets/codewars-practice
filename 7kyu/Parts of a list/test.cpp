#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"
#include <vector>
#include <utility>

using std::vector;
using std::pair;
using std::string;

void testequal(vector<pair<string, string>> ans,
               vector<pair<string, string>> sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing partline")
{
	SUBCASE("Fixed_Tests_partlist")
	{
		vector<string> s = {"cdIw", "tzIy", "xDu", "rThG"};
		vector<pair<string, string>> sol = {
			{"cdIw", "tzIy xDu rThG"}, {"cdIw tzIy", "xDu rThG"}, {"cdIw tzIy xDu", "rThG"}
		};
		vector<pair<string, string>> ans = PartList::partlist(s);
		testequal(ans, sol);

		s = {"I", "wish", "I", "hadn't", "come"};
		sol = {
			{"I", "wish I hadn't come"}, {"I wish", "I hadn't come"}, {"I wish I", "hadn't come"},
			{"I wish I hadn't", "come"}
		};
		ans = PartList::partlist(s);
		testequal(ans, sol);

		s = {"vJQ", "anj", "mQDq", "sOZ"};
		sol = {{"vJQ", "anj mQDq sOZ"}, {"vJQ anj", "mQDq sOZ"}, {"vJQ anj mQDq", "sOZ"}};
		ans = PartList::partlist(s);
		testequal(ans, sol);
	}
}
