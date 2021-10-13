#pragma once

#include <range/v3/numeric/accumulate.hpp>

/*
int Add(int x, int y)
{
	return ranges::accumulate(std::vector{x, y}, 0);
}
*/

/*
int Add(int x, int y)
{
	return y == 0 ? x : Add(x ^ y, (x & y) << 1);
}
*/

int Add(int x, int y)
{
	while (y)
	{
		int carry = x & y;
		x ^= y;
		y = carry << 1;
	}
	return x;
}
