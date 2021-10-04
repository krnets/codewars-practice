#pragma once
#include <algorithm>

// #include <range/v3/all.hpp>

#include <range/v3/view/filter.hpp>
#include <range/v3/view/take_last.hpp>
#include <range/v3/to_container.hpp>

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


/*
std::vector<int> evenNumbers(std::vector<int> arr, int n)
{
	arr.erase(std::remove_if(arr.begin(), arr.end(),
	                         [](int x) { return x % 2 != 0; }), arr.end());
	arr.erase(arr.begin(), arr.end() - n);

	return arr;
}
*/

using namespace ranges;
using std::vector;

vector<int> evenNumbers(vector<int> arr, int n)
{
	auto v = arr
		| views::filter([](int x) { return x % 2 == 0; })
		| ranges::to<vector>();

	return v | views::take_last(n) | ranges::to<vector>();
}

/*
vector<int> evenNumbers(vector<int> arr, int n)
{
	vector<int> v;

	for (auto it = arr.rbegin(); it != arr.rend(); ++it)
	{
		if (*it % 2 == 0)
		{
			v.push_back(*it);
			--n;
		}
		if (n == 0) break;
	}

	reverse(v.begin(), v.end());

	return v;
}
*/
