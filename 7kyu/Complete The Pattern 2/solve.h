#pragma once

#include <string>

std::string pattern(int n)
{
	std::string str;
	std::string ret;

	for (int i = n; i > 0; --i) str += '0' + i;

	while (n > 0)
	{
		ret += str.substr(0, n) + '\n';
		--n;
	}

	return ret.substr(0, ret.length() - 1);
}
