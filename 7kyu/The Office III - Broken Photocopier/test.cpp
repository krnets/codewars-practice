#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sample_tests")
{
	SUBCASE("Simple_cases")
	{
		CHECK(broken("01") == "10");
		CHECK(broken("001111110011001110101111101001") == "110000001100110001010000010110");
		CHECK(broken("00110100110010011100110010100111100000011") == "11001011001101100011001101011000011111100");
		CHECK(broken("00000011111010001100010101001110") == "11111100000101110011101010110001");
		CHECK(broken("0000000000") == "1111111111");
		CHECK(broken("1111111111") == "0000000000");
	}
}