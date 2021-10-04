#pragma once
#include <vector>
#include <range/v3/algorithm/min_element.hpp>

using std::vector;

/*
int findSmallest(vector<int> list)
{
	int min = INT32_MAX;

	for (const int x : list)
		if (min > x)
			min = x;

	return min;
}
*/

/*
#include <algorithm>
#include <vector>

int findSmallest(std::vector<int> list)
{
	return *min_element(list.begin(), list.end());
}
*/

int findSmallest(vector<int> list)
{
	return *ranges::min_element(list);
}
