#pragma once
#include <algorithm>
#include <iterator>
#include <vector>
#include <range/v3/range/conversion.hpp>
#include <range/v3/view/filter.hpp>

/*
std::vector<int> get_even_numbers(const std::vector<int>& arr)
{
	std::vector<int> v;

	for (int x : arr)
		if (x % 2 == 0)
			v.push_back(x);

	return v;
}
*/

/*
std::vector<int> get_even_numbers(const std::vector<int>& arr)
{
	std::vector<int> v;
	std::copy_if(arr.begin(), arr.end(), std::back_inserter(v),
	             [](int x) { return x % 2 == 0; });
	return v;
}
*/


std::vector<int> get_even_numbers(const std::vector<int>& xs)
{
	return xs
		| ranges::views::filter([](int x) { return x % 2 == 0; })
		| ranges::to<std::vector<int>>();
}
