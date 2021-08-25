#pragma once

#include <iomanip>

/*
std::string seriesSum(int n)
{
	double sum = 0;

	for (int i = 0; i < n; ++i)
		sum += 1.0 / (3 * i + 1);

	std::ostringstream oss;
	oss << std::setprecision(2) << std::fixed << sum;

	return oss.str();
}
*/

std::string seriesSum(int n)
{
	double sum = 0.005;

	for (int i = 0; i < n; ++i)
		sum += 1.0 / (3 * i + 1);

	auto s = std::to_string(sum);

	return s.substr(0, s.find('.') + 3);
}
