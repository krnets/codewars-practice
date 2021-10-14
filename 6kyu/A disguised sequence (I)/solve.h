#pragma once

#include <cmath>

/*
class HiddenSeq
{
public:
	static unsigned long long fcn(int n)
	{
		return std::pow(2, n);
	}
};
*/

class HiddenSeq
{
public:
	static unsigned long long fcn(int n)
	{
		return 1ULL << n;
	}
};
