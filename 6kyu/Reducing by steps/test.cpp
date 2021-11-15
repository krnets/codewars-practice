#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

template <typename Func>
static void dotest(Func func, std::vector<long long>& arr, long long init, std::vector<long long> expected)
{
	CHECK(Operarray::operArray(func, arr, init) == expected);
}

TEST_CASE("testing Reducing by steps")
{
	std::vector<long long> dta, sol;

	SUBCASE("operArray test 1")
	{
		dta = {18, 69, -90, -78, 65, 40};
		sol = {18, 3, 3, 3, 1, 1};
		dotest(Operarray::gcdi, dta, dta[0], sol);
		sol = {18, 414, 2070, 26910, 26910, 107640};
		dotest(Operarray::lcmu, dta, dta[0], sol);
		sol = {18, 69, 69, 69, 69, 69};
		dotest(Operarray::maxi, dta, dta[0], sol);
		sol = {18, 18, -90, -90, -90, -90};
		dotest(Operarray::mini, dta, dta[0], sol);
		sol = {18, 87, -3, -81, -16, 24};
		dotest(Operarray::som, dta, 0, sol);
	}
	SUBCASE("operArray test 2")
	{
		dta = {10, 70, -97, -84, -96, -16};
		sol = {10, 10, 1, 1, 1, 1};
		dotest(Operarray::gcdi, dta, dta[0], sol);
		sol = {10, 70, 6790, 40740, 325920, 325920};
		dotest(Operarray::lcmu, dta, dta[0], sol);
		sol = {10, 70, 70, 70, 70, 70};
		dotest(Operarray::maxi, dta, dta[0], sol);
		sol = {10, 10, -97, -97, -97, -97};
		dotest(Operarray::mini, dta, dta[0], sol);
		sol = {10, 80, -17, -101, -197, -213};
		dotest(Operarray::som, dta, 0, sol);
	}
	SUBCASE("operArray test 3")
	{
		dta = {-73, -79, 19, -15, 99, 84};
		sol = {73, 1, 1, 1, 1, 1};
		dotest(Operarray::gcdi, dta, dta[0], sol);
		sol = {73, 5767, 109573, 1643595, 54238635, 1518681780};
		dotest(Operarray::lcmu, dta, dta[0], sol);
		sol = {-73, -73, 19, 19, 99, 99};
		dotest(Operarray::maxi, dta, dta[0], sol);
		sol = {-73, -79, -79, -79, -79, -79};
		dotest(Operarray::mini, dta, dta[0], sol);
		sol = {-73, -152, -133, -148, -49, 35};
		dotest(Operarray::som, dta, 0, sol);
	}
	SUBCASE("operArray test 4")
	{
		dta = {-41, 88, 72, 45, 46, 72};
		sol = {41, 1, 1, 1, 1, 1};
		dotest(Operarray::gcdi, dta, dta[0], sol);
		sol = {41, 3608, 32472, 162360, 3734280, 3734280};
		dotest(Operarray::lcmu, dta, dta[0], sol);
		sol = {-41, 88, 88, 88, 88, 88};
		dotest(Operarray::maxi, dta, dta[0], sol);
		sol = {-41, -41, -41, -41, -41, -41};
		dotest(Operarray::mini, dta, dta[0], sol);
		sol = {-41, 47, 119, 164, 210, 282};
		dotest(Operarray::som, dta, 0, sol);
	}
}
