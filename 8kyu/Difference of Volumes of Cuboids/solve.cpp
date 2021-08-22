#include <array>
#include <numeric>
#include <functional>

/*
int findDifference(std::array<int, 3> a, std::array<int, 3> b)
{
	int mult_a = 1;
	int mult_b = 1;

	for (int x : a) mult_a *= x;
	for (int x : b) mult_b *= x;

	return abs(mult_a - mult_b);
}
*/


int findDifference(std::array<int, 3> a, std::array<int, 3> b)
{
	return std::abs(
		std::accumulate(a.begin(), a.end(), 1, std::multiplies<int>()) -
		std::accumulate(b.begin(), b.end(), 1, std::multiplies<int>()));
}
