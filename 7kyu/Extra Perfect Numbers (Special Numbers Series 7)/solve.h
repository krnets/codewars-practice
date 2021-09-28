#pragma once

#include <vector>

/*
std::vector<int> extraPerfect(int number)
{
	std::vector<int> v;

	for (int i = 1; i <= number; ++i)
		if ((i & 1) == 1)
			v.push_back(i);

	return v;
}
*/


std::vector<int> extraPerfect(int number)
{
	std::vector<int> v;

	for (int i = 1; i <= number; ++i)
		if (i & 0x10001)
			v.push_back(i);

	return v;
}
