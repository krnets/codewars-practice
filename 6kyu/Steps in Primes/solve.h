#pragma once

#include <cmath>
#include <range/v3/view/iota.hpp>
#include <range/v3/view/filter.hpp>
#include <range/v3/view/take.hpp>
#include <range/v3/front.hpp>

using namespace ranges;

using LL = long long;

/*
class StepInPrimes
{
public:
	static bool is_prime(LL n)
	{
		if (n <= 1) return false;
		if (n <= 3 || n == 5) return true;
		if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;

		LL limit = sqrt(n);

		for (LL i = 5; i <= limit; i += 6)
			if (n % i == 0 || n % (i + 2) == 0)
				return false;

		return true;
	}

	static std::pair<LL, LL> step(int g, LL m, LL n)
	{
		auto is_prime_and_step = [g](LL x) { return is_prime(x) && is_prime(x + g); };

		auto view = views::closed_iota(m, n)
			| views::filter(is_prime_and_step)
			| views::take(1);

		return view.empty() ? std::make_pair(0ll, 0ll) : std::make_pair(front(view), front(view) + g);
	}
};
*/

class StepInPrimes
{
public:
	static bool is_prime(LL n)
	{
		if (n == 2 || n == 3 || n == 5) return true;
		if (n < 2 || n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;

		for (LL i = 5; i <= sqrt(n); i += 6)
			if (n % i == 0 || n % (i + 2) == 0)
				return false;

		return true;
	}

	static std::pair<LL, LL> step(int g, LL m, LL n)
	{
		while (m++ < n)
			if (is_prime(m) && is_prime(m + g))
				return {m, m + g};

		return {0, 0};
	}
};
