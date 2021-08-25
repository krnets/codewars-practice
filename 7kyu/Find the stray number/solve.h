#pragma once
#include <unordered_map>

/*
int stray(std::vector<int> numbers)
{
	std::map<int, int> map;

	for (int x : numbers)
		map[x]++;

	for (auto pair : map)
		if (pair.second == 1)
			return pair.first;

	return 0;
}
*/

int stray(std::vector<int> numbers)
{
	std::unordered_map<int, int> umap;

	for (int x : numbers)
		umap[x]++;

	for (auto pair : umap)
		if (pair.second == 1)
			return pair.first;

	return 0;
}

/*
int stray(std::vector<int> numbers)
{
	int unique = 0;

	for (int number : numbers)
	{
		unique ^= number;
	}

	return unique;
}
*/

