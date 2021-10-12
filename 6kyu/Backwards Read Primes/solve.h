#pragma once

#include <cmath>
#include <range/v3/algorithm/reverse.hpp>
#include <range/v3/range/conversion.hpp>
#include <range/v3/view/filter.hpp>
#include <range/v3/view/iota.hpp>
#include <range/v3/view/join.hpp>
#include <range/v3/view/transform.hpp>

using namespace ranges;
using std::string;
using std::vector;

/*
class BackWardsPrime
{
public:
	static bool is_prime(int n)
	{
		if (n <= 1) return false;
		if (n <= 3 || n == 5) return true;
		if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;
		int limit = sqrt(n);

		for (int i = 5; i <= limit; i += 6)
			if (n % i == 0 || n % (i + 2) == 0)
				return false;

		return true;
	}

	static string backwardsPrime(long long start, long long end)
	{
		vector<int> primes = views::closed_iota(start, end) | views::filter(is_prime) | to<vector<int>>();

		auto is_backwards_prime = [&](int n)
		{
			string s = std::to_string(n);
			string t = s;
			reverse(s);

			return s != t && is_prime(std::stoi(s));
		};

		vector<string> filtered = primes
			| views::filter(is_backwards_prime)
			| views::transform([](int n) { return std::to_string(n); })
			| to<vector<string>>();

		return filtered | views::join(' ') | to<string>();
	}
};
*/

class BackWardsPrime
{
public:
	static bool is_prime(int n)
	{
		if (n <= 1) return false;
		if (n <= 3 || n == 5) return true;
		if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;
		int limit = sqrt(n);

		for (int i = 5; i <= limit; i += 6)
			if (n % i == 0 || n % (i + 2) == 0)
				return false;

		return true;
	}

	static string backwardsPrime(long long start, long long end)
	{
		auto is_backwards_prime = [](long long n)
		{
			string s = std::to_string(n);
			string t = s;
			reverse(s);

			return s != t && is_prime(std::stoll(s));
		};

		vector<string> filtered = views::closed_iota(start, end)
			| views::filter(is_prime)
			| views::filter(is_backwards_prime)
			| views::transform([](long long n) { return std::to_string(n); })
			| to<vector<string>>();

		return filtered | views::join(' ') | to<string>();
	}
};
