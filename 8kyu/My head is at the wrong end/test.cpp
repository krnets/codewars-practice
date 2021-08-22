#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"
#include <array>
#include <string>

TEST_CASE("testing fixTheMeerkat")
{
	using ary = std::array<std::string, 3>;

	SUBCASE("BasicTests")
	{
		CHECK(fixTheMeerkat(ary { "tail", "body", "head" }) == ary { "head", "body", "tail" });
		CHECK(fixTheMeerkat(ary { "tails", "body", "heads" }) == ary { "heads", "body", "tails" });
		CHECK(fixTheMeerkat(ary { "bottom", "middle", "top" }) == ary { "top", "middle", "bottom" });
		CHECK(fixTheMeerkat(ary { "lower legs", "torso", "upper legs" }) == ary { "upper legs", "torso",
		      "lower legs" });
		CHECK(fixTheMeerkat(ary { "ground", "rainbow", "sky" }) == ary { "sky", "rainbow", "ground" });
	}
}
