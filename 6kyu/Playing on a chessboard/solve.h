#pragma once

class Suite2
{
public:
	static std::string game(unsigned long long n)
	{
		std::stringstream oss;
		oss << "[";

		if (n & 1)
			oss << n * n << ", 2";
		else oss << n * n / 2;

		return oss.str() + "]";
	}
};
