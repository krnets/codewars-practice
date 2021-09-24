#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing SampleTests")
{
	SUBCASE("should_pass_sample_tests")
	{
		CHECK(valid_spacing("Hello world") == true);
		CHECK(valid_spacing(" Hello world") == false);
		CHECK(valid_spacing("Hello  world ") == false);
		CHECK(valid_spacing("Hello") == true);
		CHECK(valid_spacing("Helloworld") == true);
		CHECK(valid_spacing("") == true);
	}
}
