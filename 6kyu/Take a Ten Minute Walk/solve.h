#pragma once

/*
bool isValidWalk(std::vector<char> walk)
{
	if (walk.size() != 10) return false;
	int x = 0, y = 0;

	for (auto c : walk)
	{
		switch (c)
		{
		case 'n': ++y; break;
		case 's': --y; break;
		case 'e': ++x; break;
		case 'w': --x; break;
		}
	}

	return x == 0 && y == 0;
}
*/

#include <range/v3/algorithm/count.hpp>

using namespace ranges;

bool isValidWalk(std::vector<char> walk)
{
	return walk.size() == 10 &&
		count(walk, 'n') == count(walk, 's') &&
		count(walk, 'e') == count(walk, 'w');
}
