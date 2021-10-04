#pragma once

/*
bool isAscOrder(std::vector<int> arr)
{
	for (int i = 1; i < arr.size(); ++i)
		if (arr[i] < arr[i - 1])
			return false;

	return true;
}
*/

/*
bool isAscOrder(std::vector<int> arr)
{
	return std::is_sorted(arr.begin(), arr.end());
}
*/

#include <range/v3/algorithm/is_sorted.hpp>

bool isAscOrder(std::vector<int> arr)
{
	return ranges::is_sorted(arr);
}
