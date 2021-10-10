#pragma once

#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/numeric/accumulate.hpp>

using namespace ranges;
using std::string;
using std::vector;

/*
class Kata
{
public:
	static bool validate(long long int n)
	{
		auto get_char_val = [](char c) { return c - '0'; };
		string s = std::to_string(n);
		vector<int> digits = s | views::transform(get_char_val) | to<vector<int>>();

		for (int i = digits.size() - 2; i >= 0; i -= 2)
		{
			digits[i] *= 2;

			if (digits[i] > 9)
				digits[i] -= 9;
		}
		return accumulate(digits, 0) % 10 == 0;
	}
};
*/

class Kata
{
public:
	static bool validate(long long int n)
	{
		long long int sum = 0;

		while (n > 0)
		{
			sum += n % 10;
			n /= 10;

			sum += 2 * (n % 10) - (n % 10 < 5 ? 0 : 9);
			n /= 10;
		}

		return sum % 10 == 0;
	}
};
