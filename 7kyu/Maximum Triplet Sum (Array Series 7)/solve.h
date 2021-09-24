#pragma once

#include <numeric>
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/take_last.hpp>
#include <range/v3/action/sort.hpp>
#include <range/v3/action/unique.hpp>

int maxTriSum(std::vector<int> numbers)
{
	return ranges::accumulate(numbers
	                          | ranges::views::all
	                          | ranges::actions::sort
	                          | ranges::actions::unique
	                          | ranges::views::take_last(3), 0);
}

/*
using namespace std;

int maxTriSum(vector<int> numbers)
{
	set s(numbers.begin(), numbers.end());

	return accumulate(s.rbegin(), next(s.rbegin(), 3), 0);
}
*/
