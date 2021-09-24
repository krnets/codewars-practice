#pragma once

#include <string>

std::string specialNumber(int number)
{
	while (number > 0)
	{
		int x = number % 10;

		if (x > 5)
			return "NOT!!";

		number /= 10;
	}
	return "Special!!";
}
