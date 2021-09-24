#pragma once

#include<string>
#include <range/v3/all.hpp>

std::string vaporcode(const std::string& str)
{
	std::string s;

	for (char c : str)
	{
		if (c != ' ')
		{
			s += toupper(c);
			s += "  ";
		}
	}
	return s.substr(0, s.length() - 2);
}
