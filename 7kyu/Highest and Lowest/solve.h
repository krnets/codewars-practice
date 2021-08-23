#pragma once
#include <string>
#include <sstream>

std::string highAndLow(const std::string& numbers)
{
	int min = INT32_MAX;
	int max = INT32_MIN;

	std::istringstream iss(numbers);
	std::ostringstream oss;
	std::string word;

	while (iss >> word)
	{
		int x = std::stoi(word);

		if (x < min) min = x;
		if (x > max) max = x;
	}

	oss << max << " " << min;

	return oss.str();
}


/*
std::string highAndLow(const std::string& numbers)
{
	int min = INT32_MAX;
	int max = INT32_MIN;

	std::istringstream iss(numbers);
	std::ostringstream oss;
	std::string token;

	while (std::getline(iss, token, ' '))
	{
		int x = std::stoi(token);

		if (x < min) min = x;
		if (x > max) max = x;
	}

	oss << max << " " << min;

	return oss.str();
}
*/
