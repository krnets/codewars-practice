#pragma once

#include <numeric>

/*class CountDig
{
public:
	static int nbDig(int n, int d)
	{
		int count = 0;
		char digit_char = d + '0';

		for (int i = 0; i <= n; ++i)
		{
			auto square = std::to_string(i * i);

			count += std::count_if(square.begin(), square.end(), [digit_char](char c) { return c == digit_char; });
		}

		return count;
	}
};*/

/*
class CountDig
{
public:
	static int nbDig(int n, int d)
	{
		std::vector<int> vint(n + 1);
		std::iota(vint.begin(), vint.end(), 0);
		std::vector<std::string> vstr(n + 1);

		for (int x : vint)
			vstr.push_back(std::to_string((x * x)));

		std::string digits = std::accumulate(vstr.begin(), vstr.end(), std::string());

		return std::count(digits.begin(), digits.end(), d + '0');
	}
};

*/
/*
class CountDig
{
public:
	static int nbDig(int n, int d)
	{
		int count = 0;

		for (int i = 0; i <= n; ++i)
		{
			int square = i * i;

			do
			{
				if (square % 10 == d)
					count++;

				square /= 10;
			}
			while (square > 0);
		}

		return count;
	}
};
*/

/*
class CountDig
{
public:
	static int nbDig(int n, int d)
	{
		std::string digits;

		for (int i = 0; i <= n; ++i)
			digits.append(std::to_string(i * i));

		return std::count(digits.begin(), digits.end(), d + '0');
	}
};
*/

class CountDig
{
public:
	static int nbDig(int n, int d)
	{
		int count = !d;

		for (int i = 1; i <= n; ++i)
		{
			for (int m = i * i; m > 0; m /= 10)
			{
				count += (m % 10 == d);
			}
		}

		return count;
	}
};
