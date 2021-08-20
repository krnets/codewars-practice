#include <vector>
#include <cstdint>
#include <cmath>

/*
std::vector<uint64_t> powers_of_two(int n)
{
	std::vector<uint64_t> vec;
	vec.reserve(n + 1);

	for (int i = 0; i <= n; ++i)
	{
		vec.push_back(pow(2, i));
	}

	return vec;
}
*/

std::vector<uint64_t> powers_of_two(int n)
{
	std::vector<uint64_t> vec;
	uint64_t x = 1;

	for (int i = 0; i <= n; ++i)
	{
		vec.push_back(x);
		x = x << 1;
	}
	return vec;
}
