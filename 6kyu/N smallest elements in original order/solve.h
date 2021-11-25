#pragma once

/*
using std::vector;

vector<int> firstNSmallest(const vector<int> arr, int n)
{
	vector<int> res;

	if (n == 0) return res;

	const int sz = n;
	std::map<int, int> map1, map2;

	for (int x : arr)
		map1[x]++;

	for (auto [key, val] : map1)
	{
		while (val > 0)
		{
			map2[key]++;
			--val;
			--n;

			if (n == 0) break;
		}
		if (n == 0) break;
	}

	for (int x : arr)
	{
		if (map2[x])
		{
			res.push_back(x);
			map2[x]--;
		}
		if (res.size() == sz)
			break;
	}

	return res;
}
*/

#include <range/v3/algorithm/partial_sort.hpp>

using std::vector;

vector<int> firstNSmallest(const vector<int> arr, int n)
{
	vector<int> vec, aux(arr);

	ranges::partial_sort(aux, aux.begin() + n);
	std::map<int, int> map;
	aux.resize(n);

	for (int x : aux)
		map[x]++;

	for (int x : arr)
	{
		if (map[x] > 0)
		{
			vec.push_back(x);
			map[x]--;
		}
		if (vec.size() == n)
			break;
	}
	return vec;
}
