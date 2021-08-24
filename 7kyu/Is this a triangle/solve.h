#pragma once

/*
namespace Triangle
{
	bool isTriangle(int a, int b, int c)
	{
		return a - b < c && b - c < a && c - a < b;
	}
}
*/

namespace Triangle
{
	bool isTriangle(int a, int b, int c)
	{
		if (a <= 0 || b <= 0 || c <= 0) return false;

		if (unsigned(a) + unsigned(b) <= unsigned(c)) return false;
		if (unsigned(b) + unsigned(c) <= unsigned(a)) return false;
		if (unsigned(c) + unsigned(a) <= unsigned(b)) return false;

		return true;
	}
}
