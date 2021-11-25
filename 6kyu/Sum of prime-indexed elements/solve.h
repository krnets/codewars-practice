#pragma once

bool is_prime(int n)
{
	if (n == 2 || n == 3 || n == 5) return true;
	if (n < 2 || n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;

	int limit = sqrt(n);

	for (int i = 5; i <= limit; i += 6)
		if (n % i == 0 || n % (i + 2) == 0)
			return false;

	return true;
}

int solve(std::vector<int> v)
{
	int sum = 0;

	for (int i = 0; i < v.size(); ++i)
		if (is_prime(i))
			sum += v[i];

	return sum;
}
