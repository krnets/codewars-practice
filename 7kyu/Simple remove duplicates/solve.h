#pragma once
#include <map>
#include <unordered_set>
#include <vector>

/*
std::vector<int> solve(std::vector<int> vec)
{
	std::map<int, int> freq;
	std::vector<int> res;

	for (int x : vec)
		freq[x]++;

	for (int x : vec)
		if (freq[x] == 1)
			res.push_back(x);
		else freq[x]--;

	return res;
}
*/


std::vector<int> solve(std::vector<int> vec)
{
	std::unordered_set uset(vec.rbegin(), vec.rend());
	vec.assign(uset.begin(), uset.end());
	std::reverse(vec.begin(), vec.end());

	return vec;
}
