#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <random>
#include"../../doctest.h"
#include"solve.cpp"

TEST_CASE("testing")
{
	SUBCASE("should_work_for_sample_test")
	{
		CHECK(SubtractSum(10) =="apple");
	}
	SUBCASE("Random_Tests")
	{
		std::default_random_engine gen;

		for (int i = 0; i < 100; i++)
		{
			int m = gen() % 9990 + 11;
			CHECK(SubtractSum(m) == "apple");
		}
	}
}
