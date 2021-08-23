#pragma once
#include <cmath>

bool approx_equals(double a, double b)
{
	double EPS = 0.001;

	return abs(a - b) < EPS;
}
