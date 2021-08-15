#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing GradeBook")
{
	SUBCASE("ShouldReturnA")
	{
		CHECK(getGrade(95, 90, 93) == 'A');
		CHECK(getGrade(100, 85, 96) == 'A');
		CHECK(getGrade(92, 93, 94) == 'A');
		CHECK(getGrade(100, 100, 100) == 'A');
	}
	SUBCASE("ShouldReturnB")
	{
		CHECK(getGrade(70, 70, 100) == 'B');
		CHECK(getGrade(82, 85, 87) == 'B');
		CHECK(getGrade(84, 79, 85) == 'B');
	}
	SUBCASE("ShouldReturnC")
	{
		CHECK(getGrade(70, 70, 70) == 'C');
		CHECK(getGrade(75, 70, 79) == 'C');
		CHECK(getGrade(60, 82, 76) == 'C');
	}
	SUBCASE("ShouldReturnD")
	{
		CHECK(getGrade(65, 70, 59) == 'D');
		CHECK(getGrade(66, 62, 68) == 'D');
		CHECK(getGrade(58, 62, 70) == 'D');
	}
	SUBCASE("ShouldReturnF")
	{
		CHECK(getGrade(44, 55, 52) == 'F');
		CHECK(getGrade(48, 55, 52) == 'F');
		CHECK(getGrade(58, 59, 60) == 'F');
		CHECK(getGrade(0, 0, 0) == 'F');
	}
}
