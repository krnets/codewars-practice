#pragma once

#include <vector>

#include <range/v3/algorithm/sort.hpp>

/*
int nthSmallest(std::vector<int> passed, int nSmallest)
{
	ranges::sort(passed);

	return passed[nSmallest - 1];
	// return passed.at(nSmallest - 1);
}
*/

int nthSmallest(std::vector<int> passed, int nSmallest)
{
	auto nth = std::next(passed.begin(), nSmallest - 1);
	std::nth_element(passed.begin(), nth, passed.end());

	return *nth;
}

/*
int nthSmallest(std::vector<int> passed, int nSmallest)
{
	auto nth = std::next(passed.begin(), nSmallest - 1);
	std::ranges::nth_element(passed, nth);

	return *nth;
}
*/
