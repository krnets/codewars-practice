#pragma once

#include <unordered_map>

using std::vector;

/*
vector<int> deleteNth(vector<int> arr, int n)
{
	std::unordered_map<int, int> map;

	for (int x : arr)
	{
		if (map.find(x) == map.end())
			map[x] = 1;
		else if (map[x] < n)
			map[x]++;
	}

	vector<int> ans;

	for (int x : arr)
	{
		if (map[x] > 0)
		{
			ans.push_back(x);
			--map[x];
		}
	}
	return ans;
}
*/

vector<int> deleteNth(vector<int> arr, int n)
{
	std::map<int, int> map;
	vector<int> res;

	for (int x : arr)
		if (map[x]++ < n)
			res.push_back(x);

	return res;
}
