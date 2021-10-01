#pragma once

/*
std::pair<int, int> solve(int s, int g)
{
	if (s % g != 0)
		return std::make_pair(-1, -1);

	return std::make_pair(g, s - g);
}
*/
using std::make_pair;

std::pair<int, int> solve(int s, int g)
{
	return (s % g == 0) ? make_pair(g, s - g) : make_pair(-1, -1);
}
