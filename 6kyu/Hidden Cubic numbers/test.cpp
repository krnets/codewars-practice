#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

using std::string;

static void dotest(string& str, string expected)
{
	CHECK(Cubes::isSumOfCubes(str) == expected);
}

TEST_CASE("testing Hidden Cubic numbers")
{
	string s;

	SUBCASE("isSumOfCubes_Test 1")
	{
		s = "&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()";
		dotest(s, "407 407 Lucky");
	}
	SUBCASE("isSumOfCubes_Test 2")
	{
		s = "0 9026315 -827&()";
		dotest(s, "0 0 Lucky");
	}
	SUBCASE("isSumOfCubes_Test 3")
	{
		s = "aqdf&0#1xyz!22[153(777.777";
		dotest(s, "0 1 153 154 Lucky");
	}
	SUBCASE("isSumOfCubes_Test 4")
	{
		s = "QK29a45[&erui9026315";
		dotest(s, "Unlucky");
	}
}
