#pragma once
#include <algorithm>
#include <iterator>
#include <vector>

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

std::vector<int> get_even_numbers(const std::vector<int>& arr)
{
	std::vector<int> v;
	std::copy_if(arr.begin(), arr.end(), std::back_inserter(v),
	             [](int x) { return x % 2 == 0; });
	return v;
}
