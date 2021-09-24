#pragma once

#include <cmath>

std::string disariumNumber(int number)
{
	std::string digits = std::to_string(number);
	int sum = 0;

	for (size_t i = 0; i < digits.length(); ++i)
	{
		sum += pow(digits[i] - '0', i + 1);
	}

	return sum == number ? "Disarium !!" : "Not !!";
}
