#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void do_test(int width, const std::string& ratio, const std::string& expected)
{
	CHECK(find_screen_height(width, ratio) == expected);
}

TEST_CASE("testing sample_test")
{
	SUBCASE("example_tests")
	{
		do_test(1024, "4:3", "1024x768");
		do_test(1280, "16:9", "1280x720");
		do_test(3840, "32:9", "3840x1080");
	}
}
