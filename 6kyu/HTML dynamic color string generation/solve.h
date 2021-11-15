#pragma once
#include <iomanip>

struct GenerateColorRGB
{
	static std::string generateColor(int randomNumber)
	{
		std::ostringstream oss;
		oss << '#' << std::hex << std::setw(6) << randomNumber % 0xFFFFFF;

		return oss.str();
	}
};
