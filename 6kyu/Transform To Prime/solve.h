#pragma once

#include <cmath>
#include <range/v3/numeric/accumulate.hpp>

bool is_prime(int n)
{
	if (n == 2 || n == 3 || n == 5) return true;
	if (n < 2 || n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;

	for (int i = 5; i <= std::sqrt(n); i += 6)
		if (n % i == 0 || n % (i + 2) == 0)
			return false;

	return true;
};

int next_prime(int n)
{
	while (!is_prime(n)) ++n;

	return n;
};

int minimumNumber(std::vector<int> numbers)
{
	int sum = ranges::accumulate(numbers, 0);

	return next_prime(sum) - sum;
}
