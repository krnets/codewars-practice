#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing SampleTests")
{
	SUBCASE("should_pass_sample_tests")
	{
		using v = std::vector<int>;
		CHECK(solve({ "abode", "ABc", "xyzD" }) == v{ 4, 3, 1 });
		CHECK(solve({ "abide", "ABc", "xyz" }) == v{ 4, 3, 0 });
		CHECK(solve({ "IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc" }) == v{ 6, 5, 7 });
		CHECK(solve({ "encode", "abc", "xyzD", "ABmD" }) == v{ 1, 3, 1, 3 });
		CHECK(solve({}) == v{});
	}
}
