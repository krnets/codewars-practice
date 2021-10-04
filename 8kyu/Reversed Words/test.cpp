#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing SampleTests")
{
	SUBCASE("should_pass_sample_tests")
	{
		CHECK(reverse_words("hello world!") == "world! hello");
		CHECK(reverse_words("yoda doesn't speak like this") == "this like speak doesn't yoda");
		CHECK(reverse_words("foobar") == "foobar");
		CHECK(reverse_words("kata editor") == "editor kata");
		CHECK(reverse_words("row row row your boat") == "boat your row row row");
		CHECK(reverse_words( "The greatest victory is that which requires no battle") ==
			"battle no requires which that is victory greatest The");
	}
}
