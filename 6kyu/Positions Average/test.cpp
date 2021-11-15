#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"
#include <iomanip>

void assertFuzzy(const std::string& s, double expect)
{
	std::cout << std::setprecision(10);
	std::cout << std::scientific;
	double merr = 1e-9;
	std::cout << "Testing: " << s << std::endl;
	double actual = posAverage(s);
	std::cout << "Actual: " << actual << std::endl;
	std::cout << "Expect: " << expect << std::endl;
	bool inrange = std::abs(actual - expect) <= merr;

	if (inrange == false)
		std::cout << "Expected: " << expect << ", got " << actual << std::endl;

	std::cout << inrange << std::endl;
	CHECK(inrange == true);
}

TEST_CASE("testing Positions Average")
{
	SUBCASE("Tests_positionAverage")
	{
		assertFuzzy("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096", 26.6666666667);
		assertFuzzy("444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490", 29.2592592593);
		assertFuzzy("4444444, 4444444, 4444444, 4444444, 4444444, 4444444, 4444444, 4444444", 100);
	}
}
