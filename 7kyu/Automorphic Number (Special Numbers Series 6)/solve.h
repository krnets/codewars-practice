#pragma once

#include <string>

std::string autoMorphic(int number)
{
	long square = number * number;

	while (number > 0)
	{
		int x = number % 10;
		number /= 10;

		int y = square % 10;
		square /= 10;

		if (x != y)
			return "Not!!";
	}

	return "Automorphic";
}
