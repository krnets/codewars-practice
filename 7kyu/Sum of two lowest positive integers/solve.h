#pragma once
#include <vector>

/*
long sumTwoSmallestNumbers(std::vector<int> numbers)
{
	std::sort(numbers.begin(), numbers.end());

	return numbers[0] + numbers[1];
}
*/

long sumTwoSmallestNumbers(std::vector<int> numbers)
{
	long lowOne = std::numeric_limits<long>::max();
	long lowTwo = lowOne;

	for (int number : numbers)
	{
		if (number < lowOne)
		{
			lowTwo = lowOne;
			lowOne = number;
		}
		else if (number < lowTwo)
			lowTwo = number;
	}

	return lowOne + lowTwo;
}
