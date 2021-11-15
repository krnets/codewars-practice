#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing md5 hash decoding")
{
	SUBCASE("simple_pin")
	{
		string actual = crack("827ccb0eea8a706c4c34a16891f84e7b");
		CHECK(actual == "12345");
	}
	SUBCASE("harder_pin")
	{
		string actual = crack("86aa400b65433b608a9db30070ec60cd");
		CHECK(actual == "00078");
	}
}
