#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing reverse strings")
{
	SUBCASE("Check_Short_Words")
	{
		CHECK(reverseString("hello") == "olleh");
		CHECK(reverseString("rat") == "tar");
		CHECK(reverseString("alpha") == "ahpla");
	}
	SUBCASE("Check_Longer_Words")
	{
		CHECK(reverseString("codewars") == "srawedoc");
		CHECK(reverseString("football") == "llabtoof");
		CHECK(reverseString("translation") == "noitalsnart");
	}
}
