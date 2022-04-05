#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Roman Numerals Encoder")
{
	SUBCASE("sample tests")
	{
		CHECK("CLXXXII" == solution(182));
		CHECK("MCMXC"== solution(1990));
		CHECK("MDCCCLXXV"== solution(1875));
	}
	SUBCASE("one_yields_I")
	{
		CHECK("I" == solution(1));
	}

	SUBCASE("two_yields_II")
	{
		CHECK("II" == solution(2));
	}

	SUBCASE("three_yields_III")
	{
		CHECK("III" == solution(3));
	}

	SUBCASE("four_yields_IV")
	{
		CHECK("IV" == solution(4));
	}

	SUBCASE("five_yields_V")
	{
		CHECK("V" == solution(5));
	}

	SUBCASE("six_yields_VI")
	{
		CHECK("VI" == solution(6));
	}

	SUBCASE("nine_yields_IX")
	{
		CHECK("IX" == solution(9));
	}

	SUBCASE("twenty_seven_yields_XXVII")
	{
		CHECK("XXVII" == solution(27));
	}

	SUBCASE("forty_eight_yields_XLVIII")
	{
		CHECK("XLVIII" == solution(48));
	}

	SUBCASE("fifty_nine_yields_LIX")
	{
		CHECK("LIX" == solution(59));
	}

	SUBCASE("ninety_three_yields_XCIII")
	{
		CHECK("XCIII" == solution(93));
	}

	SUBCASE("one_hundred_forty_one_yields_CXLI")
	{
		CHECK("CXLI" == solution(141));
	}

	SUBCASE("one_hundred_sixty_three_yields_CLXIII")
	{
		CHECK("CLXIII" == solution(163));
	}

	SUBCASE("four_hundred_two_yields_CDII")
	{
		CHECK("CDII" == solution(402));
	}

	SUBCASE("five_hundred_seventy_five_yields_DLXXV")
	{
		CHECK("DLXXV" == solution(575));
	}

	SUBCASE("nine_hundred_eleven_yields_CMXI")
	{
		CHECK("CMXI" == solution(911));
	}

	SUBCASE("one_thousand_twenty_four_yields_MXXIV")
	{
		CHECK("MXXIV" == solution(1024));
	}

	SUBCASE("three_thousand_yields_MMM")
	{
		CHECK("MMM" == solution(3000));
	}
}
