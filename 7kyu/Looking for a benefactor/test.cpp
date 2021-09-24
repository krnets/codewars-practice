#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing newavg_basic_tests")
{
	SUBCASE("should_work")
	{
		std::vector<double> arr1 = {14.0, 30.0, 5.0, 7.0, 9.0, 11.0, 16.0};
		CHECK(NewAverage::newAvg(arr1, 90) == 628);

		std::vector<double> arr2 = {14, 30, 5, 7, 9, 11, 15};
		CHECK(NewAverage::newAvg(arr2, 92) == 645);
	}
	SUBCASE("throw_error")
	{
		std::vector<double> arr1 = {14, 30, 5, 7, 9, 11, 15};
		CHECK_THROWS_AS(NewAverage::newAvg(arr1, 2), std::logic_error) ;
	}
}
