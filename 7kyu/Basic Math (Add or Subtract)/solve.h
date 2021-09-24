#pragma once
#include <regex>

std::string calculate(std::string str)
{
	std::regex re("(plus)|(minus)|(\\d+)");

	auto begin = std::sregex_token_iterator(str.begin(), str.end(), re);
	int acc = 0;
	std::string prev;

	for_each(begin, {}, [&](auto it)
	{
		auto token = it.str();

		if (isdigit(token[0]))
			acc += (prev == "minus" ? -stoi(token) : stoi(token));

		prev = token;
	});

	return std::to_string(acc);
}

/*
std::string calculate(std::string str)
{
	std::size_t pos = 0;
	int acc = std::stoi(str, &pos);

	while (pos < str.size())
	{
		if (str[pos] == 'p')
		{
			pos += 4;
			str = str.substr(pos);
			acc += std::stoi(str, &pos);
		}
		else
		{
			pos += 5;
			str = str.substr(pos);
			acc -= std::stoi(str, &pos);
		}
	}

	return std::to_string(acc);
}
*/
