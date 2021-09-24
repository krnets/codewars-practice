#pragma once
#include <algorithm>
#include <vector>

/*
std::vector<int> evenNumbers(std::vector<int> arr, int n)
{
	std::vector<int> vec;

	for (int i = arr.size() - 1; i >= 0; --i)
	{
		if (arr[i] % 2 == 0 && n > 0)
		{
			vec.push_back(arr[i]);
			n--;
		}
	}
	std::ranges::reverse(vec);

	return vec;
}
*/


std::vector<int> evenNumbers(std::vector<int> arr, int n)
{
	arr.erase(std::remove_if(arr.begin(), arr.end(),
	                         [](int x) { return x % 2 != 0; }), arr.end());
	arr.erase(arr.begin(), arr.end() - n);

	return arr;
}
