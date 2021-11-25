#pragma once

std::string pattern(int n)
{
	std::ostringstream oss;

	for (int i = 1; i <= n; ++i)
	{
		oss << std::string(i - 1, ' ');

		for (int j = i; j <= n; ++j)
		{
			oss << ' ' << i % 10;
		}
		if (i != n) oss << '\n';
	}
	return oss.str();
}
