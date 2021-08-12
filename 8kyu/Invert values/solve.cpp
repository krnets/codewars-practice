#include <vector>
#include <algorithm>
#include <functional>

/*
std::vector<int> invert(std::vector<int> values)
{
	for (int& value : values) value = -value;

	return values;
}
*/

/*
std::vector<int> invert(std::vector<int> values)
{
	std::transform(values.begin(), values.end(), values.begin(), [](const int& a) { return -a; });

	return values;
}
*/

std::vector<int> invert(std::vector<int> values)
{
	std::transform(values.begin(), values.end(), values.begin(), std::negate());

	return values;
}
