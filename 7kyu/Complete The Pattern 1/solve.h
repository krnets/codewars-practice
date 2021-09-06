#pragma once

/*
std::string pattern(int n)
{
	if (n == 0) return "";

	std::ostringstream oss;

	for (int i = 1; i <= n; ++i)
	{
		for (int j = 0; j < i; ++j)
		{
			oss << i;
		}
		oss << "\n";
	}

	std::string str = oss.str();
	str.pop_back();

	return str;
}
*/

std::string pattern(int n)
{
	std::ostringstream oss;
	const auto osit = std::ostream_iterator<std::string>(oss);

	for (int i = 1; i <= n; ++i)
	{
		std::fill_n(osit, i, std::to_string(i));
		oss << "\n";
	}
	std::string str = oss.str();

	return n == 0 ? str : str.erase(str.length() - 1);
}
