#include <string>
#include <algorithm>

/*
std::string fakeBin(std::string str)
{
	std::string result;

	for (char c : str)
	{
		if (c < '5')
			result += '0';
		else
			result += '1';
	}

	return result;
}
*/

std::string fakeBin(std::string str)
{
	std::transform(str.begin(), str.end(), str.begin(), [](char c) { return c < '5' ? '0' : '1'; });

	return str;
}
