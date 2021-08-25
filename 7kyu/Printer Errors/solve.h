#pragma once

#include <fmt/core.h>

/*
class Printer
{
public:
	static std::string printerError(const std::string& s)
	{
		int errorsCount = 0;

		for (char c : s)
			if (c > 'm')
				errorsCount++;

		return fmt::format("{}/{}", errorsCount, s.size());
	}
};
*/


class Printer
{
public:
	static std::string printerError(const std::string& s)
	{
		int errorsCount = std::count_if(s.begin(), s.end(), [](char c) { return c > 'm'; });

		return fmt::format("{}/{}", errorsCount, s.size());
	}
};
