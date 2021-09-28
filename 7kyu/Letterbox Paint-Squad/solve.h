#pragma once

#include <array>

/*
std::array<int, 10> paint_letterboxes(int start, int end)
{
	std::array<int, 10> arr = {0};
	std::ostringstream oss;

	for (int i = start; i <= end; ++i)
		oss << i;

	for (char c : oss.str())
		arr[c - '0']++;

	return arr;
}
*/

std::array<int, 10> paint_letterboxes(int start, int end)
{
	std::array<int, 10> arr = {0};

	for (int i = start; i <= end; ++i)
	{
		for (int n = i; n > 0; n /= 10)
		{
			arr[n % 10]++;
		}
	}
	return arr;
}

/*
std::array<int, 10> paint_letterboxes(int start, int end)
{
	std::array<int, 10> arr = {0};

	for (int i = start; i <= end; ++i)
	{
		int x = i;

		while (x > 0)
		{
			arr[x % 10]++;
			x /= 10;
		}
	}
	return arr;
}
*/
