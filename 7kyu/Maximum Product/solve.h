#pragma once
#include <cmath>
#include <algorithm>
#include <numeric>

/*

int adjacentElementsProduct(std::vector<int> inputArray)
{
	int max_product = std::numeric_limits<int>::min();

	for (int i = 1; i < inputArray.size(); ++i)
	{
		int product = inputArray[i - 1] * inputArray[i];
		max_product = std::max(product, max_product);
	}

	return max_product;
}*/

int adjacentElementsProduct(std::vector<int> inputArray)
{
	std::adjacent_difference(inputArray.begin(),
	                         inputArray.end(),
	                         inputArray.begin(),
	                         std::multiplies<int>());

	return *std::max_element(std::next(inputArray.cbegin()), inputArray.cend());
}
