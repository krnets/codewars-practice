#pragma once

/*
std::pair<std::string, std::string> capitalize(const std::string& s)
{
	std::string first, second;

	for (int i = 0; i < s.size(); ++i)
	{
		char c = s[i];

		if (i % 2 == 0)
		{
			first.push_back(::toupper(c));
			second.push_back(c);
		}
		else
		{
			first.push_back(c);
			second.push_back(::toupper(c));
		}
	}

	return std::make_pair(first, second);
}
*/

std::pair<std::string, std::string> capitalize(const std::string& s)
{
	auto p = std::make_pair(s, s);

	for (int i = 0; i < s.length(); ++i)
	{
		if (i % 2 == 0)
			p.first[i] -= 0x20;
		else
			p.second[i] -= 0x20;
	}

	return p;
}
