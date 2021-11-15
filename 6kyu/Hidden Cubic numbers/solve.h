#pragma once
#include <range/v3/all.hpp>
#include <regex>

using namespace ranges;

class Cubes
{
public:
	static bool is_cubic(int n)
	{
		int sum = 0;
		int x = n;
		while (x > 0)
		{
			int y = x % 10;
			sum += (y * y * y);
			x /= 10;
		}
		return sum == n;
	}

	static std::string isSumOfCubes(std::string& str)
	{
		std::regex re("\\d{1,3}");
		auto it = std::sregex_token_iterator(str.begin(), str.end(), re);
		auto end = std::sregex_token_iterator();
		std::ostringstream oss;
		bool cubic_found = false;
		int sum = 0;

		while (it != end)
		{
			int x = std::stoi(it->str());

			if (is_cubic(x))
			{
				oss << x << ' ';
				sum += x;
				cubic_found = true;
			}
			++it;
		}

		if (!cubic_found) return "Unlucky";

		oss << sum << " Lucky";

		return oss.str();
	}
};
