#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Piapprox")
{
	SUBCASE("test1")
	{
		string sol1 = "[10, 3.0418396189]";
		string ans1 = PiApprox::iterPi(0.1);
		CHECK(ans1 == sol1);
	}
	SUBCASE("test2")
	{
		string sol2 = "[100, 3.1315929036]";
		string ans2 = PiApprox::iterPi(0.01);
		CHECK(ans2 == sol2);
	}
	SUBCASE("test3")
	{
		string sol3 = "[1000, 3.1405926538]";
		string ans3 = PiApprox::iterPi(0.001);
		CHECK(ans3 == sol3);
	}
	SUBCASE("test4")
	{
		string sol4 = "[10000, 3.1414926536]";
		string ans4 = PiApprox::iterPi(0.0001);
		CHECK(ans4 == sol4);
	}
	SUBCASE("test5")
	{
		string sol5 = "[200, 3.1365926848]";
		string ans5 = PiApprox::iterPi(0.005);
		CHECK(ans5 == sol5);
	}
	SUBCASE("test6")
	{
		string sol6 = "[10000001, 3.1415927536]";
		string ans6 = PiApprox::iterPi(0.0000001);
		CHECK(ans6 == sol6);
	}
	SUBCASE("test7")
	{
		string sol7 = "[400, 3.1390926575]";
		string ans7 = PiApprox::iterPi(0.0025);
		CHECK(ans7 == sol7);
	}
	SUBCASE("test8")
	{
		string sol8 = "[2, 2.6666666667]";
		string ans8 = PiApprox::iterPi(0.5);
		CHECK(ans8 == sol8);
	}
}
