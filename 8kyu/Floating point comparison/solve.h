#pragma once
#include <cmath>

bool approx_equals(double a, double b)
{
	const double epsilon = 0.001;

	return std::abs(a - b) < epsilon;
}
