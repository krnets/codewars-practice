#pragma once

#include <string>
#include <vector>

std::string switcher(const std::vector<std::string>& arr)
{
	std::ostringstream oss;
	char c;

	for (auto s : arr)
	{
		int x = std::stoi(s);

		switch (x)
		{
		case 27: c = '!';
			break;
		case 28: c = '?';
			break;
		case 29: c = ' ';
			break;
		default: c = 26 - x + 'a';
		}

		oss << c;
	}

	return oss.str();
}
