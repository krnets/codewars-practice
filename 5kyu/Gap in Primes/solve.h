#pragma once

#include <cmath>
#include <unordered_set>

class GapInPrimes
{
public:
	static bool is_prime(long long n)
	{
		if (n == 2 || n == 3 || n == 5) return true;
		if (n <= 1 || n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;
		long long limit = std::sqrt(n);

		for (long long i = 5; i <= limit; i += 6)
			if (n % i == 0 || n % (i + 2) == 0)
				return false;

		return true;
	}

	/*
	static std::pair<long long, long long> gap(int g, long long m, long long n)
	{
		auto result = std::make_pair(0ll, 0ll);
		std::unordered_set<long long> non_primes;

		for (auto i = m; i <= n - g; ++i)
		{
			if (!non_primes.count(i) && is_prime(i))
			{
				bool prime_in_gap = false;

				for (long long j = i + 1; j < i + g; ++j)
				{
					if (is_prime(j))
						prime_in_gap = true;
					else non_primes.insert(j);
				}

				if (!prime_in_gap && is_prime(i + g))
				{
					result = {i, i + g};
					break;
				}
			}
		}
		return result;
	}
*/

	static std::pair<long long, long long> gap(int g, long long m, long long n)
	{
		long long last_prime = 2;

		for (auto i = m; i <= n; ++i)
		{
			if (is_prime(i))
			{
				if (i - last_prime == g)
				{
					return {last_prime, i};
				}
				last_prime = i;
			}
		}
		return {0, 0};
	}
};
