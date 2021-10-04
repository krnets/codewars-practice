#pragma once
#include <vector>

#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/filter.hpp>

/*
int positive_sum(const std::vector<int> arr)
{
	int sum = 0;

	for (const int x : arr)
		if (x > 0)
			sum += x;

	return sum;
}
*/

using namespace ranges;

int positive_sum(const std::vector<int> arr)
{
	auto is_positive = [](int x) { return x > 0; };

	return accumulate(arr | views::filter(is_positive), 0);
}
