#pragma once

#include <cmath>

bool is_prime(int n)
{
	if (n <= 1) return false;
	if (n <= 3 || n == 5) return true;
	if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;

	int limit = ceil(sqrt(n));

	for (int i = 5; i <= limit; i += 6)
		if (n % i == 0 || n % (i + 2) == 0)
			return false;

	return true;
};

int nextPrime(int n)
{
	while (!is_prime(++n)) { }

	return n;
}
