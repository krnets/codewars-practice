#pragma once

#include <unordered_map>

/*
int repeats(std::vector<int> v)
{
	std::unordered_map<int, int> map;
	int ans = 0;

	for (int x : v) map[x]++;

	for (auto kvp : map)
		if (kvp.second == 1)
			ans += kvp.first;

	return ans;
}
*/

int repeats(std::vector<int> v)
{
	std::unordered_map<int, int> map;
	int ans = 0;

	for (int x : v) map[x]++;

	for (auto [fst, snd] : map)
		if (snd == 1)
			ans += fst;

	return ans;
}
